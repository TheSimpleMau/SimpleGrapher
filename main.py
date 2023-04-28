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

#A function to resize the images of the graphs.
def resize_image(path:str, max_width:int=500, max_height:int=400)->str:
    img = Image.open(path)
    img = img.resize((max_width, max_height), resample=Image.LANCZOS)
    system_os = os.name
    match system_os:
        case "nt":
            resized_path = os.path.join(os.getcwd(), ".temp.png")
            os.system(f'attrib +h .test.png')
            img.save(resized_path)
        case "posix":
            resized_path = os.path.join(os.getcwd(), ".temp.png")
            img.save(resized_path)
    return resized_path


#A function to make a graph example in the beggining of the program.
def test_image()-> str:
    #First, we will search for the example image, so we list the files on the directory.
    files = os.listdir()
    #Then, identfy the OS for the management of the files.
    system_os = os.name
    match system_os:
        #In case that is Windows.
        case "nt":
            if '.test.png' not in files:
                Grapher(functions=["sin(x) * cos(x) * (1/x) * 10"],name_image=".test").plotting()
                os.system(f'attrib +h .test.png')
            path = os.getcwd()+"\\.test.png" 
            reszie_path = resize_image(path)
        #In case that is UNIX like system.
        case "posix":
            if '.test.png' not in files:
                Grapher(functions=["sin(x) * cos(x) * (1/x) * 10"],name_image=".test").plotting()
            path = os.getcwd()+"/.test.png"
            reszie_path = resize_image(path)
    return reszie_path

def advanceWindow():
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
    win = sg.Window(title="Configuración avanzada", layout=layout)
    while True:
        event, values = win.read()
        if event == 'exit' or event == sg.WIN_CLOSED or event == 'cancel':
            values = None
            break
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


def actions(window,event,values,__advance_settings):
    advance_settings = __advance_settings
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
    return advance_settings


def graficar(window,values,__advance_settings):
    formulas = []
    for formula in values.keys():
        if formula.startswith('inp_formula') == True and values[f'{formula}'] != '':
            formulas.append(values[f'{formula}'])
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
    errors = graph.plotting()
    if len(errors) != 0:
        window['errors'].update(errors)
    resized_path = resize_image(graph.path_to_image)
    window['graph'].update(filename=resized_path)
    # window['graph'].update(filename=graph.path_to_image)



# A function to define all the layout of the window.
def lyout():
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
    layout = lyout()
    window = sg.Window("Simple Grapher", layout)
    __advance_settings = None
    while True:
        event, values = window.read()
        if event == 'exit' or event == sg.WIN_CLOSED:
            break
        elif event == "graficar":
            # try:
            graficar(window,values,__advance_settings)
            # except:
            #     print("ERROR: Revisar que todo se haya escrito correctamente")
        else:
            __advance_settings = actions(window,event,values,__advance_settings)
    window.close()
    os.system('rm .temp.png')

if __name__ == '__main__':
    main()