# The main file is where we run our website from 


from website import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug = True)


# python main.py