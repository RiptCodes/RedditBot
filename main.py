import dearpygui.dearpygui as dpg
from redditImages import redditImageScraper

def check_sub(sender, app_data): 
    if app_data != "":
        redditImageScraper(app_data, 10, "hot", nsfw=False).start()
    else:
        print("Bye")

dpg.create_context()
dpg.create_viewport(title='Reddit Scraper', width=600, height=300)

with dpg.window(label="Reddit BOT"):
    dpg.add_input_text(label="Subreddit",callback=check_sub, default_value="Enter Subreddit")
    dpg.add_input_int(label="Limit", callback=check_sub)
    dpg.add_input_text(label="Order",default_value="Enter hot/top/new")
    dpg.add_checkbox(label="NSFW", default_value=False)
    
    dpg.add_button(label="Start")
    dpg.add_button(label="Stop")
    dpg.add_button(label="Quit")



    




dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
