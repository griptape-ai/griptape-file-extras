# Open File Tool

A tool for opening files in the user's default application.

For example, ask an agent to open an image from /path/to/image and it will display it.

```python
from dotenv import load_dotenv

from griptape.file_extras.tools.open_file_tool import OpenFileTool
from griptape.file_extras.utils.env_utils import get_env_var
from griptape.structures import Agent
from griptape.drivers import OpenAiChatPromptDriver

load_dotenv()

api_key = get_env_var( "OPENAI_API_KEY" )

TEST_IMAGE = "examples/file_extras/tools/open_file_tool/media/capybara_cloud.jpeg"

agent = Agent(
    prompt_driver=OpenAiChatPromptDriver(model="gpt-4o-mini", api_key=api_key),
    tools=[OpenFileTool()],
)

agent.run(f"Can you show me the image at {TEST_IMAGE}?")
```

will output:

```bash
[12/16/24 16:38:12] INFO     ToolkitTask 99c71112b1d945be86dcb77705f00197
                             Input: Can you show me the image at examples/file_extras/tools/open_file_tool/media/capybara_cloud.jpeg?   
[12/16/24 16:38:13] INFO     Subtask 101d59730b9d4b95983dd86ad800b9d7                                                                   
                             Actions: [                                                                                                 
                               {                                                                                                        
                                 "tag": "call_Q98RxI0Ca0iFBEnIYW2QjcUL",                                                                
                                 "name": "OpenFileTool",                                                                                
                                 "path": "open_file",                                                                                   
                                 "input": {                                                                                             
                                   "values": {                                                                                          
                                     "file_path": "examples/file_extras/tools/open_file_tool/media/capybara_cloud.jpeg"                 
                                   }                                                                                                    
                                 }                                                                                                      
                               }                                                                                                        
                             ]                                                                                                          
                    INFO     Subtask 101d59730b9d4b95983dd86ad800b9d7                                                                   
                             Response: File displayed:                                                                                  
                             *redacted*/examples/file_extras/tools/open_file_tool/media/capybara_cloud.jpeg                                                                       
[12/16/24 16:38:18] INFO     ToolkitTask de3f84ec69c74e2eb034831a23a685cd                                                               
                             Output: The image "capybara_cloud.jpeg" has been displayed successfully.                                   
```