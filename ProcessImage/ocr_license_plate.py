import imagesearch.anpr.anpr as anpr

def main(k):
    imOb = anpr.PyImageSearchANPR()
    print(imOb.minAR)



if __name__ == "__main__":
    main("test")