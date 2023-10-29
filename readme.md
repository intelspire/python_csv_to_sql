# prerequisites
1. you need to have mysql community installed 
    - if it's not installed, you can install it from [MySQL installer](https://dev.mysql.com/downloads/installer/) #for windows

2. create a virtual enviroment and activate it
    - if you don't have the virtualenv tool, install it using:

        '
            pip install virtualenv
        '
        
    - then create a virtualenv using:

        '
            virtualenv envname
        '

    - then activate it using:

        '''
            envname/Scripts/activate  #for windows    
            source envname/bin/activate #for linux
        '''

3. install all requirements using:

    '
        pip install -r requirements.txt
    '

# Create .env file
create .env file at the root directory and add all needed parameters:

    '''
        DB_USER = root
        DB_PASSWORD = ...
        DB_NAME = ...
        DB_HOST = localhost
        DB_PORT = 3306
    '''

# Run script
### you can run the script using:
    
'
uvicorn main:app
'
the source folder and destination folder is passed as a request body like:
'''
{
    "dirs": {
        "src": "...",
        "dst": "..."
    }
}
'''


or 


'
python main.py
'

the source folder and destination folder is passed as script arguments like:
'''python main.py --src "..." --dst "..."
'''