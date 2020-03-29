class KernalConvolutions(object):

    height = 0 #how many pixels above and below the center the filter references
    width = 0 #how many pixels left and right of the center the filter references
    weights = [] #the list of weights for the relative positions of the pixels to the center

    def init(self, height, width, weights):
        self.height = height
        self.width = width
        self.weights = weights

    def apply_filter(self, image):
        """Applies the filter defined by the object to the image. Assumes the image is a 2D list of integers"""

        finalArray = [[0 for j in range(0, len(image[i]))] for i in range(0, len(image))] #initializes the array to be the same dimension as image but full of zeroes
        for i in range(0, len(image)): #loops over every horizontal line of pixels
            for j in range(0, len(image[i])): #loops over ever pixel in that line
                weightedSum = 0
                sumCount = 0
                for y in range(max(0, j - self.height), min(len(image[i]) - 1, j + self.height) + 1):
                    #loops over each horizontal line referenced by the filter
                    for x in range(max(0, i - self.width), min(len(image) - 1, i + self.width) + 1):
                        #loops over each pixel referenced by the filter in the line and adds it's value times the corrosponding weight to the weighted sum
                        weightedSum += image[y][x]*self.weights[y - max(0, j - self.height)][x - max(0, i - self.width)]
                        sumCount += self.weights[y - max(0, j - self.height)][x - max(0, i - self.width)]
                #writes the average weighted value of the pixels to the final array
                finalArray[j][i] = (int)(weightedSum/sumCount)
        return finalArray

    def check_filter_dimensions(self):
        """Checks to see if the weights array is the correct dimensions. Returns True if it is, and False otherwise"""

        if len(self.weights) != self.height*2 + 1:
            return False
        for line in self.weights:
            if len(line) != self.width*2 + 1:
                return False
        return True

