import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox, QLabel, QGridLayout, QDialog, QTextEdit, QMessageBox,QSpinBox,QAbstractSpinBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from uninformedsearch import uninformed_search
from informedsearch import Astar
from helper import getInvCount
import time

class StateViewer(QDialog):
    def __init__(self, cells, cost_of_path, nodes_expanded, search_depth, running_time):
        super().__init__()

        self.setWindowTitle("Puzzle States")
        self.setGeometry(200, 200, 600, 400)

        self.layout = QVBoxLayout() 
        self.setLayout(self.layout)

        self.cells = cells
        self.current_step = 0

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.grid_layout.addWidget(self.label, 0, 0, 1, 3)

        self.cost_of_path_label = QLabel("Cost of Path: " + str(cost_of_path))
        self.nodes_expanded_label = QLabel("Nodes Expanded: " + str(nodes_expanded))
        self.search_depth_label = QLabel("Search Depth: " + str(search_depth))
        self.running_time_label = QLabel("Running Time: " + str(running_time))

        self.layout.addWidget(self.cost_of_path_label)
        self.layout.addWidget(self.nodes_expanded_label)
        self.layout.addWidget(self.search_depth_label)
        self.layout.addWidget(self.running_time_label)

        self.prev_button = QPushButton("Previous Step")
        self.prev_button.clicked.connect(self.prev_step)
        self.layout.addWidget(self.prev_button)

        self.next_button = QPushButton("Next Step")
        self.next_button.clicked.connect(self.next_step)
        self.layout.addWidget(self.next_button)

        self.update_state()

    def prev_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.update_state()

    def next_step(self):
        if self.current_step < len(self.cells) - 1:
            self.current_step += 1
            self.update_state()

    def update_state(self):
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        state = self.cells[self.current_step]
        for i in range(3):
            for j in range(3):
                label = QLabel(str(state[i][j]))
                label.setFont(QFont("Arial", 12))
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet("QLabel{ padding: 30px; width: 100px; height:100px ; font-size: 32px; margin:0px 0px ; border: 1px solid black; background-color:white}")
                self.grid_layout.addWidget(label, i+1, j)

class PuzzleSolver(QWidget):
    def __init__(self):
        super().__init__()
        self.search_d = 0  
        self.num_explored = 0 
        self.t  = None
        self.setWindowTitle("8 Puzzle Solver")
        self.setGeometry(200, 200, 600, 400)
        
        self.inputs_array = []

        self.layout = QVBoxLayout()
        grid_layout = QGridLayout()

        for i in range(3):
            row_inputs = []
            for j in range(3):
                input_box = QSpinBox()
                input_box.setAlignment(Qt.AlignCenter)
                input_box.setStyleSheet("QSpinBox { padding: 5px; width: 100px; height:100px ; font-size: 32px; margin:0 0;}")
                input_box.setButtonSymbols(QAbstractSpinBox.NoButtons)
                input_box.setMinimum(0)
                input_box.setMaximum(8)
                grid_layout.addWidget(input_box, i, j)
                row_inputs.append(input_box)
            self.inputs_array.append(row_inputs)
        
        self.layout.addLayout(grid_layout)
        self.setLayout(self.layout)

        self.choose_algorithm_label = QLabel("Choose Search Algorithm:")
        self.choose_algorithm_label.setFixedSize(500, 20)
        self.layout.addWidget(self.choose_algorithm_label)

        self.layout.addStretch()

        self.algorithm_combobox = QComboBox()
        self.algorithm_combobox.addItem("DFS")
        self.algorithm_combobox.addItem("BFS")
        self.algorithm_combobox.addItem("A* with Euclidean Distance")
        self.algorithm_combobox.addItem("A* with Manhattan Distance")

        self.solve_button = QPushButton("Solve Puzzle")
        self.solve_button.clicked.connect(self.solve_puzzle)

        self.layout.addWidget(self.algorithm_combobox)
        self.layout.addWidget(self.solve_button)

        self.setLayout(self.layout)

        self.path_cost = QLabel("Cost of Path: ")
        self.expanded_nodes = QLabel("Nodes Expanded: ")
        self.search_depth = QLabel("Search Depth: ")
        self.running_time = QLabel("Running Time: ")
     
        #self.initial_state = ((7,2,5), (3,1,0), (6,4,8))
 
        
        self.algorithm = None
        self.cells = []


    def solve_puzzle(self):
        # Create a list to store values of all input boxes
        inputs_values = []

        # Retrieve values from input boxes and store them in inputs_values
        for row_inputs in self.inputs_array:
            for input_box in row_inputs:
                value = input_box.value()
                inputs_values.append(value)

        #print(inputs_values)
        tuple1 = tuple(inputs_values[:3])
        tuple2 = tuple(inputs_values[3:6])
        tuple3 = tuple(inputs_values[6:])
        self.initial_state = (tuple1, tuple2, tuple3)
        if getInvCount(self.initial_state) % 2 != 0:
            QMessageBox.critical(self, "No Solution", "No solution found.")
            return

        self.algorithm = self.algorithm_combobox.currentText()
        start = time.time()
        if self.algorithm == "DFS":
           ( self.actions, self.cells ), self.search_d  ,  self.num_explored = uninformed_search(self.initial_state, bfs=False)
        elif self.algorithm == "BFS":
            ( self.actions, self.cells ), self.search_d ,  self.num_explored = uninformed_search(self.initial_state, bfs=True)
        elif self.algorithm == "A* with Euclidean Distance":
             ( self.actions, self.cells ), self.search_d ,  self.num_explored =  Astar(self.initial_state, True)
        elif self.algorithm == "A* with Manhattan Distance":
             ( self.actions, self.cells ), self.search_d ,  self.num_explored=  Astar(self.initial_state, False)
        end  = time.time()
        self.t = str(round(end  - start, 4))
        self.show_states(self.t)
        self.update_stats()

    def show_states(self ,  time):
        state_viewer = StateViewer(self.cells, len(self.actions), self.num_explored , self.search_d, time)
        state_viewer.exec_()

    def update_stats(self):
        self.path_cost.setText("Cost of Path: " + str(len(self.cells)))
        self.expanded_nodes.setText("Nodes Expanded: " + str(self.num_explored))
        self.search_depth.setText("Search Depth: " + str(self.search_d))
        self.running_time.setText("Running Time: " + str(self.t))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    puzzle_solver = PuzzleSolver()
    puzzle_solver.show()
    sys.exit(app.exec_())
