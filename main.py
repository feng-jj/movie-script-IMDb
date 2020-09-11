from IMDb import IMDb
import Tkinter as tk


if __name__ == '__main__' :
    window = tk.Tk();
    action = IMDb('action')
    adventure = IMDb('adventure')
    animation = IMDb('animation')
    comedy = IMDb('comedy')
    crime = IMDb('crime')
    drama= IMDb('drama')
    family = IMDb('family')
    fantasy = IMDb('fantasy')
    horror = IMDb('horror')
    musical = IMDb('musical')
    mystery = IMDb('mystery')
    romance = IMDb('romance')
    short = IMDb('short')
    thriller = IMDb('thriller')
    war = IMDb('war')
    western = IMDb('western')
    
