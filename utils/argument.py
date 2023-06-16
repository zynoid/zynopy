from typing import Generic, Callable, TypeVar, Any, Optional, Type, Literal, get_args, get_origin
from inspect import stack

from argparse import ArgumentParser

T = TypeVar("T")

class argument(Generic[T]):

    def __init__(self, flag: str, type: Type[T] = str, default: Optional[T] = None, required: bool = False):
        code_context = stack(1)[1].code_context
        # support format:
        # * <arg> = argument(...)
        # * self.<arg> = argument(...)
        assert(code_context is not None and len(code_context) > 0), "failed to get code context"
        code = code_context[0]
        self.__name = code_context[0].strip().split(sep=" ")[0]
        if self.__name.startswith("self."):
            self.__name = self.__name.removeprefix("self.")
        self.__flag = flag
        self.__required = required

    def __get__(self, instance: Any, type_: type | None = None) -> T:
        assert hasattr(self, "__value"), "value is not set"
        return self.__value

    def __set__(self, instance: Any, value: T) -> None:
        self.__value = value

    def __call__(self, arg_def: Callable[[Any], T]) -> "argument[T]":
        return self

    # def func(self):
    #     print(self.__dict__)

if __name__ == "__main__":
    class Test:
        
        b = argument[Literal["abc", "bcd"]]("--b")
        
        def __init__(self) -> None:
            self.a = argument[Literal[1, 2]]("--a", type=int)

        def func(self):
            t = self.a.__orig_class__.__args__[0]
            print(get_origin(t))
            print(get_args(t))
            print(type(T))

    Test().func()
