/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* pre=NULL;
    struct ListNode* current=head;
    struct ListNode* next=NULL;
    while(current != NULL)
    {
        next=current->next;
        current->next=pre;
        pre=current;
        current=next;
    }
    head=pre;

    return head;
    
    
}
