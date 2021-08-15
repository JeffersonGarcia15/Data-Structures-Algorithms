
// # def myMap(lst, cb):
// #     new_list = []
    
// #     for i in range(len(lst) - 1):
// #         ele = lst[i]
// #         res = cb(ele, i, lst)
// #         new_list.append(res)
// #     return new_list


// # values = ['jeff', 'jefferson', 'adilson', 'lopez']



// # print(values)

let myMap = function (array, cb) {
    let newArray = []
    for (let ele of array) {
        let res = cb(ele, ele.indexOf(), array)
        newArray.push(res)
    }
    return newArray
}

let values = ['jeff', 'jefferson', 'adilson', 'lopez']

let testingMap = myMap(values, function (el) {
    return el.toUpperCase() + '!'
})

console.log(testingMap)