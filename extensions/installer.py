from extensions import app, request, render_template, current_user, Admin_users, redirect, flash
from flask_login import login_required


@app.route('/extesnions_codeword', methods=['POST', 'GET'])
@login_required
def codeword():
    if Admin_users.query.filter_by(user_id=current_user.id).first() != None:
        if 'code' in request.args:
            with open('extensions/__init__.py', 'r') as f:
                print(f.read(), "\n ------------------------------>")
            with open('extensions/__init__.py', 'a') as f:
                if request.args['code'] != None:
                    f.write('\n'+request.args['code'])
                    flash("Successful")
                    return redirect('/admin')
                return render_template('codeform.html')
            return render_template('codeform.html')
        return render_template('codeform.html')
    return render_template('403.html')
