######################################
###Importing all the modules needed###
######################################

#To make the graphs
import matplotlib.pyplot as plt
#To make opertations
import numpy as np
#To reconize the ecuations/functions
from sympy import sympify,Symbol,lambdify


###########################################
###Creating the class to make the graph.###
###########################################

class Grapher():
    #Defining the initial state of the class
    def __init__(self, functions: list, symbol: str = 'x', x_range: list = [-10, 10, 100], x_lim: list = [], x_axis_label:str = 'x' , y_lim: list = [], y_axis_label:str = 'y', title:str = None, grid:bool = True) -> None:
        #Setting the title of the graph if the users don't specify the name of it.
        if title == None:
            if len(functions) == 1:
                self.title = rf"${functions[0]}$" #In case of there's only one function to graph, then the title name will be the function.
            else:
                self.title = "Functions" #Otherwise, the title will be "Funcitons".
        self.symbol = symbol #The symbol to take as the "x"
        self.x_values = np.linspace(x_range[0],x_range[1], 100) #The range of numbers to calculate.
        self.x_lim = x_lim #The range of numbres to show in the graph on the x axis.
        self.x_axis_label = x_axis_label #To set the label of the x axis
        self.y_lim = y_lim #The range of numbres to show in the graph on the y axis.
        self.y_axis_label = y_axis_label #To set the label of the x axis
        self.grid = grid
        self.functions = functions #The functions to display on the graph
        self.x_symbol = Symbol(symbol) #Creating the symbol to make it python understanding it.
        self.exprs = [] #The expresions.
        for expr in functions:
            self.exprs.append(sympify(expr))
        self.fs = [] #The functions to evaluate.
        for expr in self.exprs:
            f = lambdify(self.x_symbol,expr,"numpy")
            self.fs.append(f)
        self.zeroDivisionErrors = []
    
    def ploting(self):
        #To clean, if it is the case, the previous graph.
        plt.clf()
        #Setting the title
        plt.title(self.title)
        #Setting the x label
        plt.xlabel(self.x_axis_label)
        #Setting the y label
        plt.ylabel(self.y_axis_label)
        #Setting the grid
        plt.grid(self.grid)
        #Setting the x lim
        if len(self.x_lim) != 0:
            plt.xlim(self.x_lim)
        #Setting the y lim
        if len(self.y_lim) != 0:
            plt.xlim(self.y_lim)
        
        #Plotting the functions
        for idx,f in enumerate(self.fs):
            y_values = f(self.x_values)
            for value in y_values:
                #In case that the function in the range ploted has a zero division error, will be reported.
                if np.isinf(value):
                    self.zeroDivisionErrors.append(f"WARNING: posible zero division error on the range of the function {self.functions[idx]} at the value of x {self.x_values[idx]}")
            plt.plot(self.x_values,y_values)
        if len(self.zeroDivisionErrors) > 0 :
            for error in self.zeroDivisionErrors:
                print(error)
        plt.show()


# Test
if __name__ == '__main__':
    xd = Grapher(["x**2 + 2"])
    xd.ploting()