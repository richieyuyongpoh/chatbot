
import dill


activateFile = 'initAIChatBotHelper.pkl'
infile = open(activateFile,'rb')

initAIChatBotHelperModule = dill.load(infile)
infile.close()

initAIChatBotHelperModule()
