from abc import ABC

# #[Factory Design Pattern] Build a logging system using the Factory Design Pattern. 
# # Create a LoggerFactory class that generates different types of loggers (e.g., FileLogger, ConsoleLogger, DatabaseLogger). 
# # Implement methods in each logger to write logs to their respective destinations. 
# # Show how the Factory Design Pattern helps to decouple the logging system from the application and allows for flexible log handling

class Logger(ABC):
    def write_log(self, message):
        pass

# File Logger
class FileLogger(Logger):
    def write_log(self, message):
        with open('logfile.txt', 'a') as file:
            file.write(message + "\n")
        print("Log written to file")

# Console Logger
class ConsoleLogger(Logger):
    def write_log(self, message):
        print("Console Log:", message)

# Database Logger
class DatabaseLogger(Logger):
    def write_log(self, message):
        print("Log written to database")

# Logger Factory
class LoggerFactory:
    def create_logger(logger_type):
        if logger_type == 'file':
            return FileLogger()
        elif logger_type == 'console':
            return ConsoleLogger()
        elif logger_type == 'database':
            return DatabaseLogger()
        else:
            raise ValueError("Unknown logger type")

# # Main code
file_type = input("Log type? file, console, database: ")
message = input("What is your message? ")

logger = LoggerFactory.create_logger(file_type)
logger.write_log(message)

# # [Builder Design Pattern] Design a document generator using the Builder Design Pattern. 
# # Create a DocumentBuilder that creates documents of various types (e.g., PDF, HTML, Plain Text). 
# # Implement the builder methods to format the document content and structure according to the chosen type. 
# # Demonstrate how the Builder Design Pattern allows for the creation of different document formats without tightly coupling the document generation logic.

class DocumentBuilder(ABC):
    def set_title(self, title):
        pass

    def set_content(self, content):
        pass

    def get_document(self):
        pass

class PDFDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = "PDF Document\n"

    def set_title(self, title):
        self.document += f"Title: {title}\n"

    def set_content(self, content):
        self.document += f"Content: {content}\n"

    def get_document(self):
        return self.document

class HTMLDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = "<html>\n"

    def set_title(self, title):
        self.document += f"<head><title>{title}</title></head>\n"

    def set_content(self, content):
        self.document += f"<body>{content}</body>\n"

    def get_document(self):
        self.document += "</html>"
        return self.document

class PlainTextDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = "Plain Text Document\n"

    def set_title(self, title):
        self.document += f"Title: {title}\n"

    def set_content(self, content):
        self.document += f"Content: {content}\n"

    def get_document(self):
        return self.document

class DocumentDirector:
    def __init__(self, type):
        if type == "pdf":
            self.builder = PDFDocumentBuilder()
        elif type == "html":
            self.builder = HTMLDocumentBuilder()
        else:
            self.builder = PlainTextDocumentBuilder()
            
    def construct_document(self, title, content):
        self.builder.set_title(title)
        self.builder.set_content(content)
        return self.builder.get_document()
    
file_type = input("What is the required document type: pdf, html, text? ")
title = input("Title? ")
content = input("Content? ")

director = DocumentDirector(file_type)
document = director.construct_document(title, content)
print(document)

# # # [Singleton Design Pattern] Implement a configuration manager using the Singleton Design Pattern. 
# # # The configuration manager should read configuration settings from a file and provide access to these settings throughout the application. 
# # # Demonstrate how the Singleton Design Pattern ensures that there is only one instance of the configuration manager, preventing unnecessary multiple reads of the configuration file.

import json

class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance.config = {}
        return cls._instance

    def load_config(self, path):
        with open(path, 'r') as file:
            self.config = json.load(file)
            if not isinstance(self.config, dict):
                raise ValueError("Configuration file must contain a JSON object.")
        print("Configuration loaded from file")
        
    def get_config(self, key):
        return self.config.get(key)

# Example usage
config_manager1 = ConfigurationManager()
config_manager1.load_config('config.json')
print(config_manager1.get_config('setting1'))

config_manager2 = ConfigurationManager()
print(config_manager2.get_config('setting2'))

# Ensuring only one instance exists
print(config_manager1 is config_manager2)  # Output: True
