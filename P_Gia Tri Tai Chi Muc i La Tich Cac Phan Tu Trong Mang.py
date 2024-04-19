def product_except_self(nums):
    n = len(nums)
    result = [1] * n # Khởi tạo mảng kết quả với tất cả các phần tử bằng 1
    
    # Tính tích của tất cả các phần tử bên trái của phần tử tại vị trí i
    left_product = 1
    for i in range(n):
        result[i] *= left_product
        left_product *= nums[i]
        
    # Tính tích của tất cả các phần tử bên phải của phần tử tại vị trí i và nhân với kết quả đã tính ở bước trước 
    right_product = 1
    for i in range(n -1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
        
    return result

# Test
nums1 = [1, 2, 3, 4, 5]
nums2 = [3, 2, 1]
print(product_except_self(nums1))  # Output: [120, 60, 40, 30, 24]
print(product_except_self(nums2))  # Output: [2, 3, 6]    