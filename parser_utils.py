import requests
from bs4 import BeautifulSoup
import json

_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Pragma': 'no-cache'
}
_URL = 'https://www.allrecipes.com/recipes/96/salad/'


def fetch_raw(recipe_url):
    """
    Fetch raw Markup for each recipe link

    Args:
        recipe_url: link to each recipe
    """
    html = None
    try:
        r = requests.get(recipe_url, _HEADERS)
        assert r.status_code == 200
        html = r.text
    except Exception as exception:
        print(str(exception))

    finally:
        return html.strip()


def get_recipes(num_recipes=10):
    """
    Fetch raw markups for all recipes as a list from a url
    """
    recipes = []
    try:
        r = requests.get(_URL, headers=_HEADERS)
        assert r.status_code == 200
        html = r.text
        soup = BeautifulSoup(html, features='lxml')
        links = soup.select('.fixed-recipe-card__h3 a')
        index = 0
        for link in links:
            print("Fetching Recipe for this link --> ", link['href'])
            recipe = fetch_raw(link['href'])
            recipes.append(recipe)
            index += 1
            if index == num_recipes:
                break

    except Exception as exception:
        print(str(exception))

    finally:
        return recipes



def parse_as_json(markup):
    """    
    Parse each raw markup as a json 

    Args:
        markup: raw markup for each recipe 

    Returns:
        JSON type object containing essential fields
    """
    title = '-'
    submit_by = '-'
    description = '-'
    calories = 0
    ingredients = []

    try:
        soup = BeautifulSoup(markup, features='lxml')
        title_section = soup.select('.recipe-summary__h1')
        submitter_section = soup.select('.submitter__name')
        description_section = soup.select('.submitter__description')
        ingredients_section = soup.select('.recipe-ingred_txt')
        calories_section = soup.select('.calorie-count')

        if calories_section:
            calories = calories_section[0].text.replace('cals', '').strip()

        if ingredients_section:
            for ingredient in ingredients_section:
                ingredient_text = ingredient.text.strip()
                if ingredient_text not in ['', 'Add all ingredients to list']:
                    ingredients.append(ingredient_text)

        if description_section:
            description = description_section[0].text.strip().replace('"', '')

        if submitter_section:
            submit_by = submitter_section[0].text.strip()

        if title_section:
            title = title_section[0].text

        record = {
            'title': title,
            'submitter': submit_by,
            'description': description,
            'calories': calories,
            'ingredients': ingredients
        }

    except Exception as ex:
        print(str(ex))

    finally:
        return json.dumps(record)
