# Import libraries
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
import seaborn as sns

# Page Options for for the overall app 
ui.page_opts(title="PyShiny App with Plot",fillable=True)

# Sidebar with slider input
with ui.sidebar():
    # Create a sidebar with a slider input for number of bins
    ui.input_slider("selected_number_of_bins", "Number of bins", 0, 100, 20)

#Define plot for rendering histogram
@render.plot(alt="A histogram")
def histogram():
    #Generate random data for demostrastion
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    #Create histogram with user input number of bins
    plt.hist(x, input.selected_number_of_bins(), density=True)
    
    #Set labels and title 
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.title('Distribution Chart')
    
    #Show the plot 
    plt.show()
