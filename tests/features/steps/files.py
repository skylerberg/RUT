# pylint: disable=import-error, unused-argument, unused-import, function-redefined
from uuid import uuid4
from os import remove

from behave import given, when, then, step

from rut.pane import Pane
from rut.controller import Controller

@given('I have a file called {name}')
def step_impl(context, name):
    context.file_name = 'tests/fixtures/' + name

@given('I have a pane with "{text}"')
def step_impl(context, text):
    context.pane = Pane(contents=text)

@given("I open a new file")
def step_impl(context):
    context.file_name = "/tmp/" + uuid4().hex
    context.pane = Pane(path=context.file_name)
    context.controller = Controller(pane=context.pane)

@when("I enter {command}")
def step_impl(context, command):
    try:
        context.controller.send_keys(command)
        context.controller.send_keys("\n")
    except SystemExit:
        context.exception = SystemExit

@when('I open it')
def step_impl(context):
    context.pane = Pane(path=context.file_name)

@when('I save it to a new file')
def step_impl(context):
    context.file_name = "/tmp/" + uuid4().hex
    context.pane.save_as(context.file_name)

@when("I modify the file")
def step_impl(context):
    context.pane.append("New content")

@when("I save the file")
def step_impl(context):
    context.pane.save()

@then('its contents will be available')
def step_impl(context):
    with open(context.file_name) as file_:
        assert str(context.pane) == file_.read()

@then("the modifications are saved")
def step_impl(context):
    with open(context.file_name) as file_:
        assert str(context.pane) == file_.read()

@then('the file will contain "{text}"')
def step_impl(context, text):
    with open(context.file_name) as saved_file:
        assert saved_file.read() == text
    remove(context.file_name)

@then(u'the program ends')
def step_impl(context):
    assert context.exception == SystemExit

@then(u'the file is saved')
def step_impl(context):
    with open(context.file_name) as file_:
        assert str(context.pane) == file_.read()

@then(u'the file is saved as PATH')
def step_impl(context):
    with open("PATH") as file_:
        assert str(context.pane) == file_.read()

