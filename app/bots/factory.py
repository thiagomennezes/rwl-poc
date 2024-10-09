from app.bots.adder import AdderBot
from app.bots.printer import PrinterBot

class FactoryBot:

    ADDER = "ADDER"
    PRINTER = "PRINTER"
    #TODO: Implement the other bots

    @staticmethod
    def create(bot):
        if bot == FactoryBot.ADDER:
            return AdderBot()
        elif bot == FactoryBot.PRINTER:
            return PrinterBot()
        #TODO: Implement the other bots
        else:
            raise Exception("{bot} not found!")