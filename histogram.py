import pandas as pd
import sys
import argparse
if __name__ == '__main__':
    if len(sys.argv)>2:
        if len(sys.argv)>3:
            column=int(sys.argv[2])
            filename=sys.argv[3]
        else:
            column=int(sys.argv[1][2])
           
            filename=sys.argv[2]
    else:
        column=2+1
        filename=sys.argv[1]
    
    print(column)
    print(filename)
    df=pd.read_csv(filename,sep="\t")
    
    print(df)
    import matplotlib.pyplot as plt
    
    hist = df.iloc[:,column].hist(bins=100)
    plt.hist(df.iloc[:,column])
    plt.savefig('histogram.png')
    plt.show()