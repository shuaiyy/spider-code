def get_size(driver):
    window_size = driver.get_window_size()
    return (
        window_size['width'],
        window_size['height']
    )


# 向左边滑动
def swipe_left(driver):
    (width, height) = get_size(driver)
    x1 = width / 10 * 9
    y1 = height / 2
    x = width / 10
    driver.swipe(x1, y1, x, y1, 2000)


# 向右边滑动
def swipe_right(driver):
    (width, height) = get_size(driver)
    x1 = width / 10
    y1 = height / 2
    x = width / 10 * 9
    driver.swipe(x1, y1, x, y1, 2000)


# 向上滑动
def swipe_up(driver):
    (width, height) = get_size(driver)
    x1 = width / 2
    y1 = height / 10 * 5
    y = height / 10
    driver.swipe(x1, y1, x1, y, 1000)


# 向下滑动
def swipe_down(driver):
    (width, height) = get_size(driver)
    x1 = width / 2
    y1 = 700
    y = 900
    driver.swipe(x1, y1, x1, y)


def tap_search(driver):
    (width, height) = get_size(driver)
    if width == 720 and height == 1440:
        driver.tap([(670, 1300)])
    elif width == 1080 and height == 1920:
        driver.tap([(1000,1830)])
    else:
        driver.tap([(670,1300)])


def swiping(driver, direction):
    if direction == 'up':
        swipe_up(driver)
    elif direction == 'down':
        swipe_down(driver)
    elif direction == 'left':
        swipe_left(driver)
    else:
        swipe_right(driver)

if __name__ == '__main__':
    print(int(1300 / 1440 * 1080))