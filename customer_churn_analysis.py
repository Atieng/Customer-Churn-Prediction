# import pandas as pd

# class CustomerChurnDataset:
    
#     def __init__(self, file_path):
#         self.df = pd.read_csv(file_path)

#     def df_info(self):
#         return self.df.info()
        
#     def statistical_summary(self):
#         return self.df.describe()

#     def get_columns(self):
#         return self.df.columns

#     def get_dtypes(self):
#         return self.df.dtypes

#     def df_shape(self):
#         return self.df.shape

#     def get_head(self, n=5):  
#         return self.df.head(n)
import pandas as pd

class CustomerChurnDataset:
    
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def df_info(self):
        print("Dataset Info:")
        print(self.df.info())
        
    def statistical_summary(self):
        print("Statistical Summary of the Dataset:")
        print(self.df.describe())

    def get_columns(self):
        print("Columns of the Dataset:")
        print(self.df.columns)

    def get_dtypes(self):
        print("Data Types of Columns:")
        print(self.df.dtypes)

    def df_shape(self):
        print("Shape of the Dataset:")
        print(self.df.shape)

    def get_head(self, n=5):  
        print("First few rows of the dataset:")
        print(self.df.head(n))

 

 
         

 
