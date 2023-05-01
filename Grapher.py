######################################
###Importing all the modules needed###
######################################

#To make the graphs
import matplotlib.pyplot as plt
#To make opertations
import numpy as np
#To reconize the ecuations/functions
from sympy import sympify,Symbol,lambdify
#To handel the save of the images
import os
#To replace some characters to other to show it the best in the legend
import re

###########################################
###Creating the class to make the graph###
###########################################

class Grapher():
    #Defining the initial state of the class
    def __init__(self, functions: list,
                 symbol: str = 'x',
                 x_range: list = [-10, 10, 100], 
                 x_lim: list = [], 
                 x_axis_label:str = 'x',
                 y_lim: list = [], 
                 y_axis_label:str = 'y',
                 title:str = None, 
                 grid:bool = True, 
                 name_image:str = None,
                 colors:list = [],
                 box_inches='Expanded') -> None:
        '''
        functions -> A list of functions that will be displayed on the graph.
        symbol -> A string representing the symbol used for the independent variable (default value: 'x').
        x_range -> A list of three values [start, stop, num] representing the range of values for the independent variable and the number of points to be generated (default value: [-10, 10, 100]).
        x_lim -> A list of two values [x_min, x_max] representing the limits for the independent variable (default value: []).
        x_axis_label -> A string representing the label for the x-axis (default value: 'x').
        y_lim -> A list of two values [y_min, y_max] representing the limits for the dependent variable (default value: []).
        y_axis_label -> A string representing the label for the y-axis (default value: 'y').
        title -> A string representing the title of the graph (default value: None).
        grid -> A boolean value representing whether to display grid lines on the graph (default value: True).
        name_image -> A string representing the name of the image file to be saved (default value: None).
        colors -> A list of colors to be used for each function (default value: []). If no colors are provided, a default set of colors will be used.
        box_inches -> To set the inches of the box that encapsulates the graph. The default value is exapanded, can be tight.
        '''
        self.title = title
        self.name_image = name_image
        self.colors = colors #The colors of each function/ecuation.
        # To set the inches of the box that encapsulates the graph.
        if box_inches == 'Expanded':
            self.box_inches = None
        else:
            self.box_inches = box_inches.lower() # To set the inches of the box that encapsulates the graph.
        self.symbol = symbol #The symbol to take as the "x"
        self.x_values = np.linspace(x_range[0],x_range[1], 1000) #The range of numbers to calculate.
        self.x_lim = x_lim #The range of numbres to show in the graph on the x axis.
        self.x_axis_label = x_axis_label #To set the label of the x axis
        self.y_lim = y_lim #The range of numbres to show in the graph on the y axis.
        self.y_axis_label = y_axis_label #To set the label of the x axis
        self.grid = grid
        self.functions = functions #The functions to display on the graph
        self.x_symbol = Symbol(symbol) #Creating the symbol to make it python understanding it.
        self.exprs = [sympify(expr) for expr in functions] #The expresions.
        self.fs = [] #The functions to evaluate.
        for expr in self.exprs:
            f = lambdify(self.x_symbol,expr,"numpy")
            self.fs.append(f)
        self.zeroDivisionErrors = [] #To archive the possibles errors
        self.path_to_image = '' #The path to the image generated.
        self.set_title()
        self.set_name_image()
    

    def pretty_text(self,texto):
        # The next functions are for show properly the ecuation/function on the legend of the graph.
        # A function to replace the exp to an e to show it properly.
        def replace_exp(match):
            return "e^{" + match.group(1) + "}"
        # A function to replace the division to a properly format to show.
        def replace_division(match):
            return "\\frac{" + match.group(1) + "}{" + match.group(2) + "}"
        def replace_power(match):
            return match.group(1) + "^{" + match.group(2) + "}"
        def replace_multiplication(match):
            return match.group(1) + "" + match.group(2)
        def replace_sqrt(text):
            return re.sub(r'sqrt\((.+?)\)', r'\\sqrt{\1}', text)
        
        set_text = re.sub(r"(\w+)\s*\*\s*(\w+)", replace_multiplication, texto) # to replace the multiplication
        set_text = re.sub(r"(\w+)\*\*([\w/*]+)", replace_power, set_text) # to replace the power
        set_text = re.sub(r"log(\d+)", r"log_{\1}", set_text) # to replace the log
        set_text = re.sub(r"exp\((.+?)\)", replace_exp, set_text) # to replace the e value
        set_text = re.sub(r"\((\d+)/(\w+)\)", replace_division, set_text) # to replace the fractions
        set_text = replace_sqrt(set_text)
        return set_text


    def set_title(self):
        #Setting the title of the graph if the users don't specify the name of it.
        if self.title is None:
            if len(self.functions) == 1:
                # self.title = fr'${self.functions[0].replace("**","^").replace("/","÷")}$' #In case of there's only one function to graph, then the title name will be the function.
                self.title = self.pretty_text(self.functions[0])
                self.title = fr'${self.title}$'
            else:
                self.title = "Functions" #Otherwise, the title will be "Funcitons".
        else:
            self.title = self.title

    def set_name_image(self):
        # To save the files and, in case of the user don't choose a name for the image, don't overwrite the saved
        if self.name_image == None and len(self.functions) == 1: #In case that there's only one funciton, the name of the image will be the function
            files = os.listdir()
            self.name_image = self.functions[0].replace("$","").replace("/","÷") #To save the name of the image. Replacing the diagonal (/) to the simbol of division
            k = 0
            while True:
                base_name = os.path.splitext(self.name_image)
                for file in files:
                    if file == self.name_image or file == f'{base_name} - {k}.png':
                        k+=1
                        self.name_image = f'{base_name} - {k}.png'
                if self.name_image not in files:
                    break
        elif self.name_image == None and len(self.functions) > 1: #In case that there's more thant one function/ecuation showing on the graph, we will be naming it as "Function"
            files = os.listdir()
            self.name_image = "Functions"
            base_name = "Functions"
            i = 0
            for file in files:
                if file == self.name_image+'.png' or file == self.name_image+f' - {i}'+'.png':
                    i+=1
                    self.name_image = f'{base_name} - {i}'
        else: #In case that the user specifies the name of the image
            self.name_image = self.name_image
    
    #Function to plot the image
    def plotting(self):
        '''
        The function to generate the image of the function.
        '''
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
            plt.ylim(self.y_lim)
        y_min = 0
        y_max = 0
        #Plotting the functions
        for idx,f in enumerate(self.fs):
            y_values = f(self.x_values)
            for value in y_values:
                #In case that the function in the range ploted has a zero division error, will be reported.
                if np.isinf(value):
                    self.zeroDivisionErrors.append(f"WARNING: posible zero division error on the range of the function {self.functions[idx]} at the value of x {self.x_values[idx]}")
                if y_min > value:
                    y_min = value
                if y_max < value:
                    y_max = value
            legend = False
            if len(self.functions) > 1 and self.title != rf"${self.functions[0]}$":
                set_legend = self.pretty_text(self.functions[idx]) #the equation/function to be modify to show it properly
                if len(self.colors) != 0 and len(self.colors) == len(self.functions):
                    plt.plot(self.x_values,y_values,label=fr'${set_legend}$',color=self.colors[idx])
                    legend = True
                else:
                    plt.plot(self.x_values,y_values,label=fr'${set_legend}$')
                    legend = True
            else:
                if len(self.colors) != 0:
                    plt.plot(self.x_values,y_values,color=self.colors[0])
                else:
                    plt.plot(self.x_values,y_values)
        if legend:
            plt.legend()
        plt.savefig(f'{self.name_image}.png',bbox_inches=self.box_inches,dpi=600)
        # plt.show()
        if os.name == 'posix':
            self.path_to_image = os.getcwd()+f'/{self.name_image}.png'
        else:
            self.path_to_image = os.getcwd()+f'\{self.name_image}.png'
        if len(self.zeroDivisionErrors) > 0 :
            for error in self.zeroDivisionErrors:
                print(error)
            return self.zeroDivisionErrors
        return ""


# Test
if __name__ == '__main__':
    ''' Only to tests '''
    functions = ["sqrt(x)", "sin(x**2) * 5", "-1/x", "log(x/5) + x**2 + 1/x", "exp(x/2)","x**2 + (1/x) - (x)"]
    symbol = 'x'
    x_range = [0.1, 5, 100]
    x_axis_label = 'x-axis'
    y_axis_label = 'y-axis'
    title = 'Test Graph'
    grid = False
    graph = Grapher(functions=functions, symbol=symbol, x_range=x_range, x_axis_label=x_axis_label, y_axis_label=y_axis_label, title=title, grid=grid)
    errors = graph.plotting()