import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials
    
            
    """
    
    #       A binomial distribution is defined by two variables: 
    #           the probability of getting a positive outcome
    #           the number of trials
    
    #       If you know these two values, you can calculate the mean and the standard deviation
    #       
    #       For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    #       You can then calculate the mean and standard deviation with the following formula:
    #           mean = p * n
    #           standard deviation = sqrt(n * p * (1 - p))
    
    #       
    
    def __init__(self, prob=.5, size=20):
        # Initialise the attributes
       
        self.p = prob
        self.n = size
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
    
    def calculate_mean(self):
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """

        self.mean = 1 * self.p * self.n 
        return self.mean

    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        
        self.stdev = math.sqrt((1 - self.p) * self.n * self.p)
        return self.stdev 
        
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """        

        #           updates the n attribute of the binomial distribution
        #           updates the p value of the binomial distribution by calculating the
        #               number of positive trials divided by the total trials
        #           updates the mean attribute
        #           updates the standard deviation attribute

        self.n = len(self.data)
        self.p = 1 * sum(self.data) / self.n
        self.calculate_mean()
        self.calculate_stdev()
        return self.p, self.n
        
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        
        plt.bar(x = [0,1], height = [(1- self.p) * self.n , self.p * self.n])
        plt.xlabel("Data")
        plt.ylabel("Frequency")
        plt.title("Histogram of the data")
        plt.show()
        
    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        a = math.factorial(self.n) / (math.factorial(k) * math.factorial(self.n-k))         
        b = (self.p ** k) * (1 - self.p) ** (self.n - k)
        return a * b 
    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        x = []
        y = []
        
        for i in self.n:
            x.append(i)
            y.append(self.pdf(i))
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')
        
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()
        return result
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
    
        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.stdev, self.p, self.n)
