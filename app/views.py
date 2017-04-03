from flask import render_template, flash, redirect, session, url_for, request, g
from app import app
from datetime import datetime
from time import sleep
from . import pi_gpio


my_pi = pi_gpio.Pi_gpio()

try:
    @app.route('/')
    def index():
        return "hello."

    @app.route('/controller')
    def controller():
        return render_template('controller.html')

    @app.route('/controller/<id>')
    def controller_id(id):
        print("in controller_id: ", id)
        if id == "all_on":
            my_pi.toggle_all(True)
        elif id == "all_off":
            my_pi.toggle_all(False)
        elif id == "preset_1":
            my_pi.toggle_all(False)
            for f in range(3):
                for i in range(1, 17):
                    my_pi.i_toggle(i)
                    sleep(0.05)
                    my_pi.i_toggle(i)
                for i in range(1, 17):
                    my_pi.i_toggle(17-i)
                    sleep(0.05)
                    my_pi.i_toggle(17-i)
        elif id == "preset_2":
            my_pi.toggle_all(False)
            for j in range(1, 17):
                if j % 2 != 0:
                    my_pi.i_toggle(j)
            sleep(0.2)
            for j in range(16):
                for j in range(1, 17):
                    my_pi.i_toggle(j)
                sleep(0.2)
            my_pi.toggle_all(False)
        else:
            print("turning on id {}".format(id))
            my_pi.i_toggle(id)
        return "success"

except KeyInterrupt:
    my_pi.cleanup_pi()
