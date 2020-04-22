import cv2

if __name__ == '__main__':
    img = cv2.imread('D:\\Workplace\\prep_map\\test.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    img, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours),type(contours))
    print(type(contours[0]))
    print(len(contours[0]))
    print(len(contours[1]))
    print(type(img))
    #cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

    # cv2.imshow("binary", binary)
    # img, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow("binary2", binary)

    # cv2.imshow("img", img)
    #cv2.waitKey(0)
