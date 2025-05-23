###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml-py
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
import typing
from baml_py.baml_py import FieldType, EnumValueBuilder, EnumBuilder, ClassBuilder
from baml_py.type_builder import TypeBuilder as _TypeBuilder, ClassPropertyBuilder, ClassPropertyViewer, EnumValueViewer
from .globals import DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME


class TypeBuilder(_TypeBuilder):
    def __init__(self):
        super().__init__(classes=set(
          ["Answer","CalculatorAPI","Functions","MyUserMessage","PIIData","PIIExtraction","Response","Resume","Steps","SubTask","Ticket","TicketClassification","WeatherAPI",]
        ), enums=set(
          ["Priority","TicketLabel","UserMessage",]
        ), runtime=DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME)


    @property
    def Answer(self) -> "AnswerAst":
        return AnswerAst(self)

    @property
    def CalculatorAPI(self) -> "CalculatorAPIAst":
        return CalculatorAPIAst(self)

    @property
    def Functions(self) -> "FunctionsAst":
        return FunctionsAst(self)

    @property
    def MyUserMessage(self) -> "MyUserMessageAst":
        return MyUserMessageAst(self)

    @property
    def PIIData(self) -> "PIIDataAst":
        return PIIDataAst(self)

    @property
    def PIIExtraction(self) -> "PIIExtractionAst":
        return PIIExtractionAst(self)

    @property
    def Response(self) -> "ResponseAst":
        return ResponseAst(self)

    @property
    def Resume(self) -> "ResumeAst":
        return ResumeAst(self)

    @property
    def Steps(self) -> "StepsAst":
        return StepsAst(self)

    @property
    def SubTask(self) -> "SubTaskAst":
        return SubTaskAst(self)

    @property
    def Ticket(self) -> "TicketAst":
        return TicketAst(self)

    @property
    def TicketClassification(self) -> "TicketClassificationAst":
        return TicketClassificationAst(self)

    @property
    def WeatherAPI(self) -> "WeatherAPIAst":
        return WeatherAPIAst(self)





class AnswerAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Answer")
        self._properties: typing.Set[str] = set([ "answer", ])
        self._props = AnswerProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "AnswerProperties":
        return self._props


class AnswerViewer(AnswerAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class AnswerProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def answer(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("answer"))

    

class CalculatorAPIAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("CalculatorAPI")
        self._properties: typing.Set[str] = set([ "answer", ])
        self._props = CalculatorAPIProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "CalculatorAPIProperties":
        return self._props


class CalculatorAPIViewer(CalculatorAPIAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class CalculatorAPIProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def answer(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("answer"))

    

class FunctionsAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Functions")
        self._properties: typing.Set[str] = set([ "name",  "description", ])
        self._props = FunctionsProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "FunctionsProperties":
        return self._props


class FunctionsViewer(FunctionsAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class FunctionsProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def name(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("name"))

    @property
    def description(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("description"))

    

class MyUserMessageAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("MyUserMessage")
        self._properties: typing.Set[str] = set([ "role",  "content", ])
        self._props = MyUserMessageProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "MyUserMessageProperties":
        return self._props


class MyUserMessageViewer(MyUserMessageAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class MyUserMessageProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def role(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("role"))

    @property
    def content(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("content"))

    

class PIIDataAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("PIIData")
        self._properties: typing.Set[str] = set([ "index",  "dataType",  "value", ])
        self._props = PIIDataProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "PIIDataProperties":
        return self._props


class PIIDataViewer(PIIDataAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class PIIDataProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def index(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("index"))

    @property
    def dataType(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("dataType"))

    @property
    def value(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("value"))

    

class PIIExtractionAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("PIIExtraction")
        self._properties: typing.Set[str] = set([ "privateData",  "containsSensitivePII", ])
        self._props = PIIExtractionProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "PIIExtractionProperties":
        return self._props


class PIIExtractionViewer(PIIExtractionAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class PIIExtractionProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def privateData(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("privateData"))

    @property
    def containsSensitivePII(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("containsSensitivePII"))

    

class ResponseAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Response")
        self._properties: typing.Set[str] = set([ "question",  "answer", ])
        self._props = ResponseProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "ResponseProperties":
        return self._props


class ResponseViewer(ResponseAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class ResponseProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def question(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("question"))

    @property
    def answer(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("answer"))

    

class ResumeAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Resume")
        self._properties: typing.Set[str] = set([ "name",  "email",  "experience",  "skills", ])
        self._props = ResumeProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "ResumeProperties":
        return self._props


class ResumeViewer(ResumeAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class ResumeProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def name(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("name"))

    @property
    def email(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("email"))

    @property
    def experience(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("experience"))

    @property
    def skills(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("skills"))

    

class StepsAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Steps")
        self._properties: typing.Set[str] = set([ "step",  "function_name", ])
        self._props = StepsProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "StepsProperties":
        return self._props


class StepsViewer(StepsAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class StepsProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def step(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("step"))

    @property
    def function_name(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("function_name"))

    

class SubTaskAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("SubTask")
        self._properties: typing.Set[str] = set([ "id",  "name", ])
        self._props = SubTaskProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "SubTaskProperties":
        return self._props


class SubTaskViewer(SubTaskAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class SubTaskProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def id(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("id"))

    @property
    def name(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("name"))

    

class TicketAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Ticket")
        self._properties: typing.Set[str] = set([ "id",  "name",  "description",  "assignedTo",  "priority",  "subTasks",  "dependencies", ])
        self._props = TicketProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "TicketProperties":
        return self._props


class TicketViewer(TicketAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class TicketProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def id(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("id"))

    @property
    def name(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("name"))

    @property
    def description(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("description"))

    @property
    def assignedTo(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("assignedTo"))

    @property
    def priority(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("priority"))

    @property
    def subTasks(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("subTasks"))

    @property
    def dependencies(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("dependencies"))

    

class TicketClassificationAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("TicketClassification")
        self._properties: typing.Set[str] = set([ "labels", ])
        self._props = TicketClassificationProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "TicketClassificationProperties":
        return self._props


class TicketClassificationViewer(TicketClassificationAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class TicketClassificationProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def labels(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("labels"))

    

class WeatherAPIAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("WeatherAPI")
        self._properties: typing.Set[str] = set([ "city",  "time",  "temperature", ])
        self._props = WeatherAPIProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "WeatherAPIProperties":
        return self._props


class WeatherAPIViewer(WeatherAPIAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class WeatherAPIProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def city(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("city"))

    @property
    def time(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("time"))

    @property
    def temperature(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("temperature"))

    



class PriorityAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.enum("Priority")
        self._values: typing.Set[str] = set([ "LOW",  "MEDIUM",  "HIGH", ])
        self._vals = PriorityValues(self._bldr, self._values)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def values(self) -> "PriorityValues":
        return self._vals


class PriorityViewer(PriorityAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    def list_values(self) -> typing.List[typing.Tuple[str, EnumValueViewer]]:
        return [(name, EnumValueViewer(self._bldr.value(name))) for name in self._values]


class PriorityValues:
    def __init__(self, enum_bldr: EnumBuilder, values: typing.Set[str]):
        self.__bldr = enum_bldr
        self.__values = values

    

    @property
    def LOW(self) -> EnumValueViewer:
        return EnumValueViewer(self.__bldr.value("LOW"))
    

    @property
    def MEDIUM(self) -> EnumValueViewer:
        return EnumValueViewer(self.__bldr.value("MEDIUM"))
    

    @property
    def HIGH(self) -> EnumValueViewer:
        return EnumValueViewer(self.__bldr.value("HIGH"))
    

    

class TicketLabelAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.enum("TicketLabel")
        self._values: typing.Set[str] = set([ "ACCOUNT",  "BILLING",  "GENERAL_QUERY", ])
        self._vals = TicketLabelValues(self._bldr, self._values)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def values(self) -> "TicketLabelValues":
        return self._vals


class TicketLabelViewer(TicketLabelAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    def list_values(self) -> typing.List[typing.Tuple[str, EnumValueViewer]]:
        return [(name, EnumValueViewer(self._bldr.value(name))) for name in self._values]


class TicketLabelValues:
    def __init__(self, enum_bldr: EnumBuilder, values: typing.Set[str]):
        self.__bldr = enum_bldr
        self.__values = values

    

    @property
    def ACCOUNT(self) -> EnumValueViewer:
        return EnumValueViewer(self.__bldr.value("ACCOUNT"))
    

    @property
    def BILLING(self) -> EnumValueViewer:
        return EnumValueViewer(self.__bldr.value("BILLING"))
    

    @property
    def GENERAL_QUERY(self) -> EnumValueViewer:
        return EnumValueViewer(self.__bldr.value("GENERAL_QUERY"))
    

    

class UserMessageAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.enum("UserMessage")
        self._values: typing.Set[str] = set([ "SPAM",  "NOT_SPAM", ])
        self._vals = UserMessageValues(self._bldr, self._values)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def values(self) -> "UserMessageValues":
        return self._vals


class UserMessageViewer(UserMessageAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    def list_values(self) -> typing.List[typing.Tuple[str, EnumValueViewer]]:
        return [(name, EnumValueViewer(self._bldr.value(name))) for name in self._values]


class UserMessageValues:
    def __init__(self, enum_bldr: EnumBuilder, values: typing.Set[str]):
        self.__bldr = enum_bldr
        self.__values = values

    

    @property
    def SPAM(self) -> EnumValueViewer:
        return EnumValueViewer(self.__bldr.value("SPAM"))
    

    @property
    def NOT_SPAM(self) -> EnumValueViewer:
        return EnumValueViewer(self.__bldr.value("NOT_SPAM"))
    

    


__all__ = ["TypeBuilder"]