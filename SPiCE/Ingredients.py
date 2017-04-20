# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:29:36 2017

@author: yago
"""
#-------------------------------------------------------------------------------

class Ingredient(object):
    """
    Generic base class; every component in SPiCE is an Ingredient.
    Use the name of the class in the ingredient file, followed by an option (the name of a valid subclass).
    The rest of the line (as any blank lines, or lines starting with '#') is ignored.
    """
    
    contains_ingredient_classes = []
    
    def __init__(self, parameters):
        """Create some Ingredient from a dictionary."""
        self.ingredients = {}
        for ingredient_class in self.contains_ingredient_classes:
            if len(ingredient_class.__subclasses__()) == 0:
                self.ingredients[ingredient_class.__name__] = ingredient_class(parameters)
            else:
                self.ingredients[ingredient_class.__name__] = ingredient_class.create_subclass(parameters)
        
    @classmethod
    def from_file(cls, parameter_file_name):
        """Alternative constructor that reads parameters from a file."""
        
        parameters = {}
        parameter_file = open(parameter_file_name,'r')
        for line in parameter_file:
            words = line.split(None,2)
            if( len(words)>1 and words[0][0]!='#' ):
                parameters[ words[0] ] = words[1]
        parameter_file.close()
        return cls(parameters)

    @classmethod
    def create_subclass(cls, parameters):
        """Create instance of the subclass specified in the parameter dictionary."""
        subclass_name = parameters.get(cls.__name__,'Undefined')
        for subclass in cls.__subclasses__():
            if( subclass.__name__ == subclass_name ):
                return subclass(parameters)
        print 'ERROR:', subclass_name, 'is not a valid', cls.__name__
        
    @classmethod
    def class_info(cls):
        print 'The class', cls.__name__, '(options', cls.__subclasses__(),') contains', cls.contains_ingredient_classes

    def info(self):
        self.__class__.class_info()
        if len(self.contains_ingredient_classes) > 0:
            for thing in self.ingredients.values():
                thing.info()
        
#-------------------------------------------------------------------------------

class Parameter(Ingredient):
    """
    An ingredient where the option is just a certain value.
    Use the name of the parameter in the ingredient file, followed by its value.
    The rest of the line (as any blank lines, or lines starting with '#') is ignored.
    """
    default_value = None
    
    @property
    def value(self):
        print "get value of", self.__class__.__name__, self._value
        return self._value

    @value.setter
    def value(self, x):
        print "set value of", self.__class__.__name__, x
        self._value = x

    @value.deleter
    def value(self):
        print "delete", self.__class__.__name__
        del self._value
    
    def __init__(self, parameters):
        print 'Creating instance of parameter', self.__class__.__name__
        self.value = parameters.get(self.__class__.__name__, self.default_value)

# -----------------------------------------------------------------------------

class Number(Parameter):
    """
    A number within a certain allowed range.
    """
    minimum_allowed = None
    maximum_allowed = None

    @property
    def value(self):
        print "overriding get value of", self.__class__.__name__, self._value
        return self._value

    @value.setter
    def value(self, x_str):
        x = float(x_str)
        print "overriding set value of", self.__class__.__name__, x
        if self.valid(x):
            self._value = x
        else:
            self._value = self.default_value

    def valid(self, x):
        print "Check that", self.__class__.__name__, self.minimum_allowed, "<", x, "<", self.maximum_allowed
        OK_status = True
        if(self.minimum_allowed is not None):
            if(x < self.minimum_allowed):
                OK_status = False
                print "WARNING:", x, "<", self.minimum_allowed
                print " => setting", self.__class__.__name__, "to default value:", self.default_value
        if(self.maximum_allowed is not None):
            if(x > self.maximum_allowed):
                OK_status = False
                print "WARNING:", x, ">", self.maximum_allowed
                print " => setting", self.__class__.__name__, "to default value:", self.default_value
        return OK_status


class FloatNumber(Number):
    """
    A floating-point number within a certain allowed range.
    """

    @property
    def value(self):
        print "overriding get value of", self.__class__.__name__, self._value
        return self._value

    @value.setter
    def value(self, x_str):
        x = float(x_str)
        print "overriding set value of", self.__class__.__name__, x
        if self.valid(x):
            self._value = x
        else:
            self._value = self.default_value


class IntNumber(Number):
    """
    An integer number within a certain allowed range.
    """

    @property
    def value(self):
        print "overriding get value of", self.__class__.__name__, self._value
        return self._value

    @value.setter
    def value(self, x_str):
        x = int(x_str)
        print "overriding set value of", self.__class__.__name__, x
        if self.valid(x):
            self._value = x
        else:
            self._value = self.default_value

# -----------------------------------------------------------------------------
