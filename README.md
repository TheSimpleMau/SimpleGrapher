# Simple Grapher 📉📈

![Main window of the program](https://github.com/TheSimpleMau/SimpleGrapher/blob/main/Images/main_window.png)

This project is a simple graph viewer designed to be user-friendly and easy to use. It is similar to GeoGebra but with a focus on simplicity. The program is intended to help beginner Python programmers who want to explore the power of matplotlib for creating graphs and visualizations. With this program, users can easily create and view graphs of mathematical functions without needing to understand the complexities of matplotlib. The program is built using PySimpleGUI, making it accessible and intuitive for users of all levels. Whether you’re a beginner just starting out with Python or an experienced programmer looking for a simple graphing tool, this project has something for everyone.

## Installation 🦦

To install it, copy the GitHub repository.

```bash
git clone https://github.com/TheSimpleMau/SimpleGrapher
```

And make sure you have the **requirements**.
```bash
pip install -r requirements.txt
```

## Usage 👨‍💻

To start graphing, just do in your terminal at the floder where you save it:
´´´ bash
python3 main.py
´´´
And it will start

## Limitations ⛔️

- It can only do lines plots.
- Can not plot from data (csv files, personal data, etc).
- Some known bugs.


## Examples 💡

### Example of images that can be generated

<table>
  <tr>
    <td align="center"><img src="https://github.com/TheSimpleMau/SimpleGrapher/blob/main/Images/example1.png" width="500" alt="Example one graph generated"></td>
    <td align="center"><img src="https://github.com/TheSimpleMau/SimpleGrapher/blob/main/Images/example2.png" width="500" alt="Example two graph generated"></td>
  </tr>
</table>

### Differents windows on the program

#### The configuration window.

![Main window of the program](https://github.com/TheSimpleMau/SimpleGrapher/blob/main/Images/configuration_window.png)

#### Example when a fucntion has an error.

![Main window of the program](https://github.com/TheSimpleMau/SimpleGrapher/blob/main/Images/error_example.png)


## Known bugs an errors

Unfortunately, I'm not GPT-4 and I can't do a perfect code, so there are some knowns errors like:

* When clicking a times, divide, log, etc. Buttons and has more than one fuction, it always put the clicked button on the first function input bar.
* When the function has indetermitation, there's a line between the last and next point where this do not happen.
* I tried to implement a "change symbol option", where you can change the independent variable of the function. For example, if you fuction is like $f(t) = e^t$ , then in the input of the fuction you can put $e^t$ and change in the configuration window the symbol for $x$ to $t$, but it doesn't work. So it doesn't show also in the main program, but you can find it on the [Grapher.py](Grapher.py) file.


## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for more information.