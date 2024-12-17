# Metadata Tool

A tool for reading and writing metadata for image files

For example, ask an agent to read Keywords metadata from /path/to/image and it will return that data if it exists.

```python
from dotenv import load_dotenv

from griptape.file_extras.tools.metadata_tool import MetadataTool
from griptape.structures import Agent
from griptape.drivers import OpenAiChatPromptDriver

import os

load_dotenv()

key = "OPENAI_API_KEY"
if not (OPENAI_API_KEY := os.getenv(key)):
    raise ValueError(f"{key} missing")

TEST_IMAGE = "examples/file_extras/tools/metadata_tool/media/capybara_cloud_wMetadata.jpeg"

agent = Agent(
    prompt_driver=OpenAiChatPromptDriver(model="gpt-4o-mini", api_key=OPENAI_API_KEY),
    tools=[MetadataTool()],
)

agent.run( f'From the metadata for "{TEST_IMAGE}", what value is in the "Keywords" field?' )
```

will output:

```bash
[12/16/24 16:41:07] INFO     ToolkitTask 99c71112b1d945be86dcb77705f00197                                                               
                             Input: From the metadata for                                                                               
                             "examples/file_extras/tools/metadata_tool/media/capybara_cloud_wMetadata.jpeg", what value is in the       
                             "Keywords" field?                                                                                          
[12/16/24 16:41:08] INFO     Subtask 4e6577e7ff0c4cda850b49c0f629b889                                                                   
                             Actions: [                                                                                                 
                               {                                                                                                        
                                 "tag": "call_422JJ0huzb01Jab8qJtdZ0YF",                                                                
                                 "name": "MetadataTool",                                                                                
                                 "path": "read_metadata",                                                                               
                                 "input": {                                                                                             
                                   "values": {                                                                                          
                                     "image_path": "examples/file_extras/tools/metadata_tool/media/capybara_cloud_wMetadata.jpeg"       
                                   }                                                                                                    
                                 }                                                                                                      
                               }                                                                                                        
                             ]                                                                                                          
                    INFO     Subtask 4e6577e7ff0c4cda850b49c0f629b889                                                                   
                             Response: {'SourceFile': 'examples/file_extras/tools/metadata_tool/media/capybara_cloud_wMetadata.jpeg',   
                             'ExifToolVersion': 13.01, 'FileName': 'capybara_cloud_wMetadata.jpeg', 'Directory':                        
                             'examples/file_extras/tools/metadata_tool/media', 'FileSize': '371 kB', 'FileModifyDate': '2024:12:16      
                             09:42:09-08:00', 'FileAccessDate': '2024:12:16 15:43:41-08:00', 'FileInodeChangeDate': '2024:12:16         
                             09:43:12-08:00', 'FilePermissions': '-rw-r--r--', 'FileType': 'JPEG', 'FileTypeExtension': 'jpg',          
                             'MIMEType': 'image/jpeg', 'CurrentIPTCDigest': '7cc113595f41ed5f853346fe4ce86daa', 'ImageWidth': 1440,     
                             'ImageHeight': 768, 'EncodingProcess': 'Baseline DCT, Huffman coding', 'BitsPerSample': 8,                 
                             'ColorComponents': 3, 'YCbCrSubSampling': 'YCbCr4:4:4 (1 1)', 'JFIFVersion': 1.01, 'ResolutionUnit':       
                             'None', 'XResolution': 1, 'YResolution': 1, 'Keywords': ['capybara', 'sword', 'clouds', 'sun'],            
                             'ApplicationRecordVersion': 4, 'XMPToolkit': 'Image::ExifTool 13.01', 'Subject': ['capybara', 'sword',     
                             'clouds', 'sun'], 'JUMDType': '(c2pa)-0011-0010-800000aa00389b71', 'JUMDLabel': 'c2pa',                    
                             'C2PAThumbnailClaimJpegType': 'image/jpeg', 'C2PAThumbnailClaimJpegData': '(Binary data 3926 bytes, use -b 
                             option to extract)', 'C2PAAi_generated_contentSalt': 'ae4adc42b0f3d20244ad28985f7625b0',                   
                             'C2PAContent-originSalt': '05196fdcce35e64a6868b6340f6b44b1', 'C2PACreation-toolSalt':                     
                             '67282331d8ce1ee94c8f3a577f3870d1', 'ActionsAction': 'c2pa.created', 'ActionsSoftwareAgent': 'Flux.1',     
                             'ActionsDigitalSourceType': 'http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia',      
                             'Model': 'Flux.1', 'Prompt': 'AI generated image', 'Ai_generated': True, 'Creator': 'Black Forest Labs',   
                             'Tool': 'Black Forest Labs API - Flux.1', 'ExclusionsStart': 20, 'ExclusionsLength': 21065, 'Name': 'jumbf 
                             manifest', 'Alg': 'sha256', 'Hash': '(Binary data 32 bytes, use -b option to extract)', 'Pad': '(Binary    
                             data 9 bytes, use -b option to extract)', 'Title': 'sample.jpeg', 'Format': 'image/jpeg', 'InstanceID':    
                             'xmp:iid:6ba6d49e-7929-476d-b3e9-d4acdd531796', 'Claim_generator': 'Black_Forest_Labs_API c2pa-rs/0.32.7', 
                             'Claim_Generator_InfoName': ['Black Forest Labs API', 'c2pa-rs'], 'Claim_Generator_InfoVersion': '0.32.7', 
                             'Signature': 'self#jumbf=c2pa.signature', 'AssertionsUrl':                                                 
                             ['self#jumbf=c2pa.assertions/c2pa.thumbnail.claim.jpeg', 'self#jumbf=c2pa.assertions/c2pa.actions',        
                             'self#jumbf=c2pa.assertions/c2pa.ai_generated_content', 'self#jumbf=c2pa.assertions/c2pa.content-origin',  
                             'self#jumbf=c2pa.assertions/c2pa.creation-tool', 'self#jumbf=c2pa.assertions/c2pa.hash.data'],             
                             'AssertionsHash': ['(Binary data 32 bytes, use -b option to extract)', '(Binary data 32 bytes, use -b      
                             option to extract)', '(Binary data 32 bytes, use -b option to extract)', '(Binary data 32 bytes, use -b    
                             option to extract)', '(Binary data 32 bytes, use -b option to extract)', '(Binary data 32 bytes, use -b    
                             option to extract)'], 'Item0': '(Binary data 3383 bytes, use -b option to extract)',                       
                             'Item1SigTstTstTokensVal': '(Binary data 6056 bytes, use -b option to extract)', 'Item1Pad': '(Binary data 
                             5435 bytes, use -b option to extract)', 'Item2': 'null', 'Item3': '(Binary data 256 bytes, use -b option to
                             extract)', 'ImageSize': '1440x768', 'Megapixels': 1.1}                                                     
[12/16/24 16:41:09] INFO     ToolkitTask 99c71112b1d945be86dcb77705f00197                                                               
                             Output: The value in the "Keywords" field for the image "capybara_cloud_wMetadata.jpeg" is:                
                             - capybara
                             - sword        
                             - clouds        
                             - sun
```