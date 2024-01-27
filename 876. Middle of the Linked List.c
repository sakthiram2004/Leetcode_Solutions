/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
     int l=0,i;
    struct ListNode* temp=head;
    while(temp!=NULL)
    {
        temp=temp->next;
        l++;
    }
 temp=head;
    for(i=1;i<=l/2;i++)
    temp=temp->next;
    return temp;
}

