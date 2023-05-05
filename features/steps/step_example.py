import os
from dotenv import load_dotenv
from behave import given, when, then
from selenium import webdriver
from pages.google_page import GooglePage
from common_utils.driver_util import get_driver

@given('I am on the Google homepage')
def step_open_google_homepage(context):
    context.driver = get_driver()
    context.google_page = GooglePage(context.driver)
    context.google_page.driver.get('https://www.google.com')

@when('I search for "{search_term}"')
def step_search_for(context, search_term):
    context.google_page.search(search_term)

@then('the search results should contain "{search_term}"')
def step_search_results_contain(context, search_term):
    assert search_term in context.google_page.get_page_title()
    context.driver.quit()