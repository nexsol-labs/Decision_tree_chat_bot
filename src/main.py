from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Query
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
class ChatBot:
    def __init__(self):
        self.rules = {
            "greeting": {
                "pattern": ["상품 문의", "가입방법", "정보 수정(변경) 및 가입확인서 발급",'사고 접수'],
                "response1": ['풍수해 6(상품)','풍수해 3(상품)'],
                'response2':['풍수해 6(상품)','풍수해 3(상품)'],
                'response3':['정보 수정','가입확인서 발급'],
                'response4':['사고 접수 방법']

            },
            "풍수해 6(상품)": {
                "response": ['가입대상','보상(담보)내용','기타']
            },
            '풍수해 3(상품)':{
                "response": ['가입대상','보상(담보)내용','기타']
            }
     
        }

    # def process_layer_1(self, user_input):
    #     for rule in self.rules["greeting"]["pattern"]:
    #         if rule in user_input.lower():
    #             return self.rules["greeting"]["response"]
    #     return "I'm sorry, I didn't understand. Could you please rephrase?"
    def frist_layer(self,user_input):
        list_of_pattern = self.rules['greeting']['pattern']
        if user_input in list_of_pattern:
            for i in list_of_pattern:
                if i == user_input:
                    number_of_index = list_of_pattern.index(i)
                    if number_of_index == 0:
                        result = '<br/>'.join(self.rules['greeting']['response1'])
                        return result
                    elif number_of_index == 1:
                        result = '<br/>'.join(self.rules['greeting']['response2'])
                        return result
                    elif number_of_index == 2:
                        result = '<br/>'.join(self.rules['greeting']['response3'])
                        return result
                    elif number_of_index == 3:
                        result = '<br/>'.join(self.rules['greeting']['response4'])
                        return result
                    else:
                        return 'choice is not selected from given choice'
        else:
            return '자세한 내용은 저희 웹 사이트를 방문하십시오'
    def second_layer(self,user_input):
        if user_input in self.rules.keys():
            if  user_input == '풍수해 6(상품)':
                result = '<br/>'.join(self.rules['풍수해 6(상품)']['response'])
                return result
            elif user_input == '풍수해 3(상품)':
                result = '<br/>'.join(self.rules['풍수해 3(상품)']['response'])
                return result
            else:
                return 'choice is noot given in response'
        else:
            return '자세한 내용은 저희 웹 사이트를 방문하십시오'
            

def run_trail(text):
    chat = ChatBot()
    if text in chat.rules['greeting']['pattern']:
        return chat.frist_layer(text)
    elif text in chat.rules.keys():
        return chat.second_layer(text)
    else:
        return '자세한 내용은 저희 웹 사이트를 방문하십시오'

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/answer")
async def answer_question(q: str = Query(...)):
    return run_trail(q)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)