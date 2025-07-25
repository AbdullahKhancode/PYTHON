from fastapi import FastAPI 
import random

app =FastAPI()
# we will build two simple get endpoints
side_hustles=[
    "Free lancing- Earning by servicing online"
    "Web development - Creating the websites "
    "Gigital marketing- Marketing the brands digitally via internet"
    "Graphic designs- Making designs, arts and logos"
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for businesses!",
]

Important_quotes=[
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "If you don’t find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey",
    "Opportunities don’t happen. You create them. – Chris Grosser",
    "Don’t stay in bed unless you can make money in bed. – George Burns",
    "Money often costs too much. – Ralph Waldo Emerson",
    "Never depend on a single income. Make an investment to create a second source. – Warren Buffett",
    "It’s not about having lots of money. It’s about knowing how to manage it. – Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "Being rich is having money; being wealthy is having time. – Margaret Bonnano",
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift",
    "Money grows on the tree of persistence. – Japanese Proverb",
]



@app.get("/side_hustle")
def get_side_hustle(apikey:str):
    """Returns the random side hustle value"""
    if apikey != "123456789":
        return {"error ":"Invalid api key"}
    return random.choice(side_hustles)


@app.get("/Important_quotes")
def get_important_quotes(apikey:str):
    """Returns the random important quote value"""
    if apikey != "123456789":
        return {"error ":"Invalid api key"}
    return random.choice(Important_quotes)

