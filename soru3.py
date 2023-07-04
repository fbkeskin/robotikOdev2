arr = [2, -4, 11, 7, 22, -3, 7]
print("sıralanmamıs dizi: ", arr)
# selection sort
# en kucuk ogeyi tekrar tekrar sec, uygun yere yerlestir
def selection_sort(arr):
  length = len(arr)
  for i in range(length - 1):
    min = i
    for j in range(i, length):
      if (arr[j] < arr[min]):
        min = j;
    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp;
selection_sort(arr)
print("\nselection sort: ", arr)


arr1 = [2, -4, 11, 7, 22, -3, 7]
# bubble sort
# yuksek degerli ogeler saga, dusuk degerli ogeler sola iterasyon mantıgı ile tasınır
def bubble_sort(arr):
  length = len(arr)
  for i in range(length):
    for j in range(1, length - i):
      if (arr[j - 1] > arr[j]):
        temp = arr[j]
        arr[j] = arr[j - 1]
        arr[j - 1] = temp
bubble_sort(arr1)
print("bubble sort: ", arr1)


arr2 = [2, -4, 11, 7, 22, -3, 7]
# insertion sort
# sıralanmıs dizi yerinde olusturulur, ogeler dogru konuma sıgdırılmak icin kaydırılır
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
insertion_sort(arr2)
print("insertion sort: ", arr2)


arr3 = [2, -4, 11, 7, 22, -3, 7]
# merge sort
# daha kucuk arrayleri sırala, sonra merge et
def merge_sort(arr):
    #dizide bir eleman varsa
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    #sort left half, then sort right half
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
print("merge sort: ", merge_sort(arr3))


arr4 = [2, -4, 11, 7, 22, -3, 7]
# quick sort
# pivotumu solundakinden küçük, sağındakinden büyük olduğu konuma getiriyorum.
def quick_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # pivot, dizinin orta elemanı secilmis olup bu kısım istege baglıdır.
    # genelde best case p = median durumunda gecerlidir.
    pivot = arr[len(arr) // 2]

    # pivot elemanından küçük, pivot elemanına eşit ve pivot elemanından büyük olanları ayırma
    smaller = []
    equal = []
    larger = []
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)

    # parçaları ayrı ayrı sıralama
    sorted_smaller = quick_sort(smaller)
    sorted_larger = quick_sort(larger)

    # parçaları merge etme
    return sorted_smaller + equal + sorted_larger
print("quick sort: ", quick_sort(arr4))
