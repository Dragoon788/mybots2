from pyrosim.commonFunctions import Save_Whitespace

class MATERIAL: 

    def __init__(self, color_name, color_code):

        self.depth  = 3

        self.string1 = color_name

        self.string2 = color_code

        self.string3 = '</material>'

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )
