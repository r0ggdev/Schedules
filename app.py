from manager import DriverManager
import time

def main():
    web = 'https://google.com'
    
    manager = DriverManager()
    manager.get(web)



# Run the main function
if __name__ == '__main__':
    main()