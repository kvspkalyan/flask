from flask import Flask, render_template, flash, redirect, url_for
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, Email

app2 = Flask(__name__)
app2.config['SECRET_KEY'] = 'kalyan'
app2.config['MAIL_PORT'] = 587
app2.config['MAIL_SERVER'] = 'smtp.gmail.com'
app2.config['MAIL_USE_TLS'] = True
app2.config['MAIL_USERNAME'] = 'darklord8722@gmail.com'
app2.config['MAIL_PASSWORD'] = 'sgqb sito bggh ynxv'
mail = Mail(app2)

class EmailForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Email')

@app2.route('/')
def index():
    form = EmailForm()
    return render_template('index2.html', form=form)

@app2.route('/send_email', methods=['POST'])
def send_mail():
    form = EmailForm()
    if form.validate_on_submit():
        recipient = form.email.data
        try:
            subject = form.subject.data
            msg = Message(subject, sender='darklord8722@gmail.com', recipients=[recipient])
            msg.body = form.message.data
            mail.send(msg)
            flash('Email sent successfully!', 'success')
        except Exception as e:
            flash(f'An error occurred while sending email: {str(e)}', 'danger')
        return redirect(url_for('index'))
    else:
        flash('Invalid email address.', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app2.run(debug=True)
