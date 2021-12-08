from extensions import app, redirect


@app.route('/home')
def main():
    return redirect('/')
