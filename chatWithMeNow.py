
import dill
import spacy

activateFile = 'initAIChatBotHelper.pkl'
infile = open(activateFile,'rb')

initAIChatBotHelperModule = dill.load(infile)
infile.close()

nlp = spacy.load("en_core_web_sm")
initAIChatBotHelperModule()
