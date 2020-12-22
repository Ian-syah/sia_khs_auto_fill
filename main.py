import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
# pip install selenium
from selenium import webdriver
from getpass import getpass

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="SIA Auto Fill")
        self.set_border_width(10)
        # self.set_size_request(200, 100)
        self._entry()
        self._initUI()
    
    def _initUI(self):
        self.set_size_request(640, 360)
        self.label = Gtk.Label("Aplikasi GTK dengan Python")
        self.add(self.label)

    def _entry(self):
        # Set The Box
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        self.add(vbox) # Add The Box to MainWindow

        # Set Username Input
        self.username = Gtk.Entry()
        self.username.set_text("")

        vbox.pack_start(self.username, False, True, 2)

        # Make Password Input
        self.password = Gtk.Entry()
        self.password.set_text("")
        self.password.set_visibility(False)

        vbox.pack_start(self.password, False, True, 2)

        # Make Sign In Button
        self.button = Gtk.Button(label="Sign In")
        self.button.connect("clicked", self._sign_in)

        vbox.pack_start(self.button, False, True, 1)

    def _sign_in(self, widget):
        driver = webdriver.Chrome("web_driver/chromedriver")

        driver.get("https://sia.unmul.ac.id/login")

        username_form = driver.find_element_by_id("exampleInputEmail")
        username_form.send_keys(self.username.get_text())

        password_form = driver.find_element_by_id("exampleInputPassword")
        password_form.send_keys(self.password.get_text())

        code_text = driver.find_element_by_css_selector("div.form-group:nth-child(3) > div:nth-child(1)").text

        security_code_form = driver.find_element_by_css_selector("div.form-group:nth-child(4) > input:nth-child(1)")
        security_code_form.send_keys(code_text)

        sign_button = driver.find_elements_by_xpath("/html/body/div/div/div/div/div/form/div[5]/button")[0]
        sign_button.click()


# main
win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

