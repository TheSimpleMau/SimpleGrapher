######################################
###Importing all the modules needed###
######################################
#To make the GUI system
import PySimpleGUI as sg
#To make the graphs
from Grapher import Grapher
#To manage the files
import os
#To resize the images
from PIL import Image

#To set all the windows with certain theme
sg.theme("Topanga")


#A function to resize the images of the graphs.
def resize_image(path:str, max_width:int=500, max_height:int=400)->str:
    '''
    This function is to show the image at the program properly.
    We'll resize the image generated and display it with the same resolution.
    This function also will save an image but it will be constantly changed.

    Arguments:
        path -> The path of the image to resize
        max_width -> The maximum width of the image
        max_height -> The maximum height of the image
    return -> str value. The path of the temporarly image.
    '''
    #To open the image in python.
    img = Image.open(path)
    #To rezise the image without losing quality.
    img = img.resize((max_width, max_height), resample=Image.LANCZOS)
    #To see in what king of OS we are.
    system_os = os.name
    if system_os == 'nt': #If the OS is Windows
        #Obtain the path to the temporarly file image.
        resized_path = os.path.join(os.getcwd(), ".temp.png")
        #We save the image.
        img.save(resized_path)
        #Also we'll hide the file.
        os.system(f'attrib +h .test.png')
    else: #If the OS is UNIX like, then...
        #Only save the path to the image
        resized_path = os.path.join(os.getcwd(), ".temp.png")
        #And save the image
        img.save(resized_path)
    # At the end, return the path to the temp image
    return resized_path


#A function to make a graph example in the beggining of the program.
def test_image()-> str:
    '''
    This function is to check if the image to graph at the very beggining exist. If the image exist, then only obtain the path to the image.
    If not, then creates the image and also obtain the path to it.
    
    No arguments.
    return -> str value. The path of the image.
    '''
    #First, we will search for the example image, so we list the files on the directory.
    files = os.listdir()
    #Then, identfy the OS for the management of the files.
    system_os = os.name
    if system_os == "nt": #For Windows systems
        if '.test.png' not in files: #If the file dosen't exist, then we will created
            Grapher(functions=["sin(x) * cos(x) * (1/x) * 10"],name_image=".test").plotting()
            #Also, we hide the file
            os.system(f'attrib +h .test.png')
        path = os.getcwd()+"\\.test.png" 
        #And save the path to that image
        reszie_path = resize_image(path)
    else: #If not a Windows system, we'll do the same logic as before but for UNIX like system.
        if '.test.png' not in files:
            Grapher(functions=["sin(x) * cos(x) * (1/x) * 10"],name_image=".test").plotting()
        path = os.getcwd()+"/.test.png"
        reszie_path = resize_image(path)
    #At the end, return the path of the image test.png
    return reszie_path


#A fuction to make the configuration windows
def advanceWindow():
    #First, we'll do all the layout with all the options
    txt_instructions = sg.Text("Modifica los siguientes valores para cambiar la gráfica.\nSi no desas modificar algún parámetro, dejalo en blanco.")
    txt_x_range = sg.Text("Rango de x")
    inp_x_range_start = sg.Input("-10", size=(4,1),key='x_range_start')
    inp_x_range_end = sg.Input("10", size=(4,1),key='x_range_end')
    inp_x_range_step = sg.Input("100", size=(4,1),key='x_range_step')
    txt_x_lim = sg.Text("Limites de x")
    inp_x_lim_left = sg.Input("", size=(4,1),key='x_lim_left')
    inp_x_lim_right = sg.Input("", size=(4,1),key='x_lim_right')
    txt_x_axis_label = sg.Text("Etiqueta del eje x")
    inp_x_axis_label = sg.Input("x",key='x_axis_label')
    txt_y_lim = sg.Text("Limites de y")
    inp_y_lim_bottom = sg.Input("", size=(4,1),key='y_lim_bottom')
    inp_y_lim_top = sg.Input("", size=(4,1),key='y_lim_top')
    txt_y_axis_label = sg.Text("Etiqueta del eje y")
    inp_y_axis_label = sg.Input("y",key='y_axis_label')
    txt_title = sg.Text("Titulo del gráfico")
    inp_title = sg.Input("",key='title')
    box_chk_grid = sg.Checkbox("Cuadrícula", default=True, key='chk_grid')
    txt_colors = sg.Text("Colores (en hexadecimal, separados por una coma)")
    inp_colors = sg.Input("", size=(20,1), key='colors')
    txt_box_inches = sg.Text("Ajustar imagen al contendio: ")
    list_box_inches = sg.Listbox(['Expanded','Tight'],default_values=['Expanded'],size=(15,2), key='box_inches')
    layout = [
        [txt_instructions],
        [txt_x_range, inp_x_range_start, sg.Text("a"), inp_x_range_end, sg.Text("en"), inp_x_range_step, sg.Text("pasos")],
        [txt_x_lim, inp_x_lim_left, sg.Text("a"), inp_x_lim_right],
        [txt_x_axis_label, inp_x_axis_label],
        [txt_y_lim, inp_y_lim_bottom, sg.Text("a"), inp_y_lim_top],
        [txt_y_axis_label, inp_y_axis_label],
        [txt_title, inp_title],
        [box_chk_grid],
        [txt_colors, inp_colors],
        [txt_box_inches,list_box_inches],
        [sg.Button("Guardar configuración", key="save"), sg.Button("Cancelar",key="cancel")]
    ]
    #Then, we'll do the actual configuration window.
    win = sg.Window(title="Configuración avanzada", layout=layout)
    while True:
        event, values = win.read()
        #If the event isn't any modification, then return None
        if event == 'exit' or event == sg.WIN_CLOSED or event == 'cancel':
            values = None
            break
        #If there's any option, then we'll check what options are and save it to return
        if event == 'save':
            none_values = [None,'']
            if values['x_range_start'] not in none_values and values['x_range_end'] not in none_values and inp_x_range_step not in none_values:
                x_range = [float(values['x_range_start']),float(values['x_range_end']),float(values['x_range_step'])]
            else:
                x_range = [-10,10,100]
            if values['x_lim_left'] not in none_values and values['x_lim_right'] not in none_values:
                x_lim = [float(values['x_lim_left']),float(values['x_lim_right'])]
            else:
                x_lim = []
            if values['x_axis_label'] != None:
                x_axis_label = values['x_axis_label']
            else:
                x_axis_label = 'x'
            if values['y_lim_bottom'] not in none_values and values['y_lim_top'] not in none_values:
                y_lim = [float(values['y_lim_bottom']),float(values['y_lim_top'])]
            else:
                y_lim = []
            if values['y_axis_label'] != None:
                y_axis_label = values['y_axis_label']
            else:
                y_axis_label = 'y'
            if values['title'] != None:
                title = values['title']
            else:
                title = None
            if values['colors'] not in none_values:
                colors = values['colors'].split(',')
            else:
                colors = []
            chk_grid = values['chk_grid']
            box_inches = values['box_inches'][0]
            values = {
                'x_range' : x_range,
                'x_lim' : x_lim,
                'x_axis_label' : x_axis_label,
                'y_lim' : y_lim,
                'y_axis_label' : y_axis_label,
                'title' : title,
                'grid' : chk_grid,
                'colors' : colors,
                'box_inches' : box_inches
            }
            break
    win.close()
    return values


#A function to do actions on the main window.
def actions(window:sg.Window,event:str,values:dict,__advance_settings:list or None) -> list or None:
    '''
    This functions is to do the difrents actions that can handle the window. It's only to intenden to make the main function more readable.
    Arguments:
        window -> A sg.Window object.
        event -> A string with the event clicked.
        values -> The values of all the inputs.
        __advance_settings -> Could be a list with all the setting of the graph or a None value if there´s no changes on the graph.
    return -> Could be a list with all the setting of the graph or a None value if there´s no changes on the graph.
    '''
    #The list or none value of the setting
    advance_settings = __advance_settings
    #All the posibles events that can happen.
    if event == "x_pow":
        window['inp_formula'].update(values['inp_formula']+'x**k')
    if event == "e_pow":
        window['inp_formula'].update(values['inp_formula']+'exp(x)')
    if event == "fraction":
        window['inp_formula'].update(values['inp_formula']+'/')
    if event == "multi":
        window['inp_formula'].update(values['inp_formula']+'*')
    if event == "plus":
        window['inp_formula'].update(values['inp_formula']+'+')
    if event == "minus":
        window['inp_formula'].update(values['inp_formula']+'-')
    if event == "log":
        window['inp_formula'].update(values['inp_formula']+'log(x)')
    if event == "sin":
        window['inp_formula'].update(values['inp_formula']+'sin(x)')
    if event == "cos":
        window['inp_formula'].update(values['inp_formula']+'cos(x)')
    if event == "tan":
        window['inp_formula'].update(values['inp_formula']+'tan(x)')
    if event == "sqrt":
        window['inp_formula'].update(values['inp_formula']+'sqrt(x)')
    if event == "abs":
        window['inp_formula'].update(values['inp_formula']+'abs(x)')
    if event == "clear":
        window['inp_formula'].update('')
    if event == "add_function":
        window.extend_layout(window,[[sg.Text("Escribe la formula: "),sg.Input("",key="inp_formula")]])
    if event == "advance_conf":
        advance_settings = advanceWindow()
    #We always return the configuration, if the user wants to use it multiple times the same configurarion.
    return advance_settings


#The function to graph.
def graph(window:sg.Window,values:dict,__advance_settings:list or None) -> None:
    '''
    This functions is to do the actual graph that will be displayed on the window.
    Arguments:
        window -> sg.Window object
        values -> The dictionary with all the values of the main window.
        __advance_settings -> The configuration of the graph.
    No returns
    '''
    #To save all the functions to be evaluated
    formulas = []
    #A for loop to check all the inputs and save every function.
    for formula in values.keys():
        if formula.startswith('inp_formula') == True and values[f'{formula}'] != '':
            formulas.append(values[f'{formula}'])
    #If there's no formulas, raise an error
    if len(formulas) == 0:
        sg.Popup("ERROR: No haz ingresado ningúna funcion para evaluar.", title="ERROR")
    else:
        #Now, we'll check if there's a name to save the graph generated  and if there's any kind of configuration at the graph.
        if values['name_file'] != '' and __advance_settings != None:
            graph = Grapher(functions=formulas,
                            name_image=values['name_file'],
                            x_range=__advance_settings['x_range'],
                            x_axis_label=__advance_settings['x_axis_label'],
                            y_lim=__advance_settings['y_lim'],
                            y_axis_label=__advance_settings['y_axis_label'],
                            title=__advance_settings['title'],
                            grid=__advance_settings['grid'],
                            colors=__advance_settings['colors'],
                            box_inches=__advance_settings['box_inches'])
        elif __advance_settings != None:
            graph = Grapher(functions=formulas,
                            x_range=__advance_settings['x_range'],
                            x_axis_label=__advance_settings['x_axis_label'],
                            y_lim=__advance_settings['y_lim'],
                            y_axis_label=__advance_settings['y_axis_label'],
                            title=__advance_settings['title'],
                            grid=__advance_settings['grid'],
                            colors=__advance_settings['colors'],
                            box_inches=__advance_settings['box_inches'])
        else:
            graph = Grapher(functions=formulas)
        #At the end, we'll plot the graph and save the error if any happen.
        errors = graph.plotting()
        #Upload the error text
        if len(errors) != 0:
            window['errors'].update(errors)
        #At the end, we'll resize the image generated to display it on the window.
        resized_path = resize_image(graph.path_to_image)
        #And update the graph on the window.
        window['graph'].update(filename=resized_path)



# A function to define all the layout of the window.
def lyout() -> list:
    '''
    This function is only intended to make the main function more readable.
    Returns the layout of the window.
    '''
    img_test_path = test_image()
    img_test = sg.Image(filename=img_test_path,key='graph')
    txt_formula = sg.Text("Escribe la formula: ")
    inp_formula = sg.Input("sin(x) * cos(x) * (1/x) * 10",key="inp_formula")
    txt_name_file = sg.Text("Escribe el nombre de la imagen: ")
    inp_name_file = sg.Input("",key="name_file")
    btn_pow = sg.Button("x^k",key='x_pow')
    btn_e_pow = sg.Button("e^k",key='e_pow')
    btn_fraction = sg.Button("/",key='fraction')
    btn_multi = sg.Button("*",key='multi')
    btn_plus = sg.Button("+",key='plus')
    btn_minus = sg.Button("-",key='minus')
    btn_log = sg.Button("log(x)",key='log')
    btn_sin = sg.Button("sin(x)",key='sin')
    btn_cos = sg.Button("cos(x)",key='cos')
    btn_tan = sg.Button("tan(x)",key='tan')
    btn_sqrt = sg.Button("sqrt(x)",key='sqrt')
    btn_abs = sg.Button("abs(x)",key='abs')
    btn_clear = sg.Button("Borrar",key='clear')
    btn_graficar = sg.Button("Graficar",key='graficar')
    txt_errors = sg.Text("",key="errors")
    btn_exit = sg.Button("Salir",key="exit")
    btn_add_function = sg.Button("Añadir función",key="add_function")
    btn_advance_conf = sg.Button("Configuración avanzada",key="advance_conf")

    layout = [
    [img_test],
    [txt_errors],
    [btn_pow, btn_e_pow, btn_fraction, btn_multi, btn_plus, btn_minus, btn_log,btn_sin, btn_cos, btn_tan, btn_sqrt, btn_abs],
    [txt_name_file,inp_name_file],
    [btn_graficar, btn_advance_conf, btn_add_function, btn_clear, btn_exit],
    [txt_formula,inp_formula]
    ]
    
    return layout


#The main function.
def main() -> None:
    '''
    Main function to do the Simple Grapher.
    '''
    #Loading the layout
    layout = lyout()
    #Makeing the main window.
    window = sg.Window("Simple Grapher", layout)
    #Initialize the configuration.
    __advance_settings = None
    #Main loop
    while True:
        #Every time, cheking the events and the values.
        event, values = window.read()
        #If the event is exit or close...
        if event == 'exit' or event == sg.WIN_CLOSED:
            #Break the main loop.
            break
        #If the event is graph.
        elif event == "graficar":
            #We'll do a try-except statment and in case of any errors, a popup showing an error will appears.
            try:
                graph(window,values,__advance_settings)
            except:
                sg.Popup("ERROR: Revisar que todo se haya escrito correctamente",title="ERROR")
        else:
            #For any other option, we'll check the actions function.
            __advance_settings = actions(window,event,values,__advance_settings)
    #When the main loop breaks, close the window.
    window.close()
    #Remove the temporarly file
    os.system('rm .temp.png')

if __name__ == '__main__':
    main()