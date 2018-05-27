/**
 * Definition for singly-linked list.
 */
function ListNode(val) {
    this.val = val;
    this.next = null;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var head = temp = null;
    var sum = 0;
    var carry = 0;
    while (l1 || l2 || carry) {
        if (l1) {
            sum += l1.val;
            l1 = l1.next;
        }
        if (l2) {
            sum += l2.val;
            l2 = l2.next;
        }
        if (carry) {
            sum += carry;
        }
        if (sum >= 10) {
            sum -= 10;
            carry = 1;
        } else {
            carry = 0;
        }
        // 首节点处理
        if (temp == null) {
            head = temp = new ListNode(sum);
        } else {
            temp.next = new ListNode(sum);
            temp = temp.next;
        }
        sum = 0;
    }
    return head;
};

var temp = l1 = new ListNode(2);
temp.next = new ListNode(4);
temp = temp.next;
temp.next = new ListNode(3);

var temp = l2 = new ListNode(5);
temp.next = new ListNode(6);
temp = temp.next;
temp.next = new ListNode(4);

function print(listnode) {
    while (listnode) {
        console.log(listnode.val);
        listnode = listnode.next;
    }
    console.log();
}

print(l1);
print(l2);
print(addTwoNumbers(l1, l2));

