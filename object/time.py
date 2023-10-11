from dataclasses import dataclass

@dataclass
class Time:
    y: str
    m: str
    d: str
    h: str
    M: str
    s: str

    def ymdhms(self) -> str:
        return f'{self.y}-{self.m}-{self.d} {self.h}:{self.M}:{self.s}'
    
    def ymd(self) -> str:
        return f'{self.y}-{self.m}-{self.d}'
    
    def hms(self) -> str:
        return f'{self.h}:{self.M}:{self.s}'

    def ymdhm(self) -> str:
        return f'{self.y}-{self.m}-{self.d} {self.h}:{self.M}'

@dataclass
class Date:
    y: str
    m: str
    d: str

    def ymd(self) -> str:
        return f'{self.y}-{self.m}-{self.d}'
    