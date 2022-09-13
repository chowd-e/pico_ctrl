def homepage(name):
    html = f"""
            <!DOCTYPE html>
            <html>
            <body>
            <head> <title>{name}</title> </head>
            <h1>Testing Board Commands </h1>
            <h2>This a brief test of the hardware command sequence</h2>
            <h3>Select a button below to command the pico board.</h3>
            <form action="/pico/led/toggle">
            <input type="submit" value="LED Toggle" />
            </form>
            <form action="/pico/led/on">
            <input type="submit" value="LED on" />
            </form>
            <form action="/pico/led/off">
            <input type="submit" value="LED off"/>
            </form>
            <p>Last command: {name}</p>
            </body>
            </html>
            """
    return str(html)