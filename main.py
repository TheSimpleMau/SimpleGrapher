#Importing all the modules needed
import PySimpleGUI as sg
from Grapher import Grapher
import os


def test_image()-> str:
    files = os.listdir()
    system_os = os.name
    match system_os:
        case "nt":
            if '.test.png' not in files:
                Grapher(functions=["sin(x)"],name_image=".test").plotting()
                os.system(f'attrib +h .test.png')
            path = os.getcwd()+"\.test.png"
        case "posix":
            if '.test.png' not in files:
                Grapher(functions=["sin(x)"],name_image=".test").plotting()
            path = os.getcwd()+"/.test.png"
    return path


def main() -> None:
    img_test_path = test_image()
    img_test = sg.Image(filename=img_test_path,key='graph')
    txt_formula = sg.Text("Escribe la formula: ")
    inp_formula = sg.Input("sin(x)",key="inp_formula")
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
    txt_errors = sg.Text("",key="erorrs")
    btn_exit = sg.Button("Salir",key="exit")

    layout = [
    [img_test],
    [btn_pow, btn_e_pow, btn_fraction, btn_multi, btn_plus, btn_minus, btn_log,btn_sin, btn_cos, btn_tan, btn_sqrt, btn_abs],
    [txt_formula, inp_formula],
    [txt_name_file,inp_name_file],
    [btn_clear, btn_graficar, btn_exit],
    [txt_errors]
    ]

    window = sg.Window("Simple Grapher", layout)
    
    while True:
        event, values = window.read()
        if event == 'exit' or event == sg.WIN_CLOSED:
            break
        if event == "x_pow":
            window['inp_formula'].update(values['inp_formula']+'x**k')
        if event == "e_pow":
            window['inp_formula'].update(values['inp_formula']+'e**k')
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
        
        if event == "graficar":
            formula = values['inp_formula']
            if values['name_file'] != '':
                graph = Grapher([formula],name_image=values['name_file'])
            else:
                graph = Grapher([formula])
            errors = graph.plotting()
            if errors != '':
                window['errors'].update(f"{errors}")
            else:
                window['graph'].update(filename=graph.name_image+'.png')

    window.close()

if __name__ == '__main__':
    main()