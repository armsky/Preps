atm 估计是面的最好的一轮了 印度大叔特别nice一口一个excellent搞的我自己都感觉自己写的不错了（错觉）
这题也简单 就是atm可以跟银行的api connect 验证用户，然后创建session如果验证成功，
session可以是一个instance放在atmclass里面做instancevariable ，login这个function就是
while(!session.valid&& attempts < 5) 重复prompt user 输入密码，然后每次whileloop都
attempts++, 超过5次就跟apiconnect 把用户锁住。我提了下state pattern大叔好像不感兴趣没让
我写。还让我写了deposit和createaccount。

有这样几个class要你implement
class AccountStore
class CardHandler
class CashDispenser
class CashIntake

然后ATM class里面有写好的menu function，就是用户输入一个选项，然后switch case到这个选项。但是你要imlement 到这个case之后的操作。比如
case LOGIN:
        //TODO: implement function to support user login

ATM有几个member
AccountStore _accountstore; // store the account created at this ATM
CardHandler _cardhanlder; // handles card read return
CashDispenser _cashdispenser; // hanldes cash dispense
CashIntake _cashintake; //

具体说一下，取款机class里有cardHandler，display，accountStore，cardDeposit等class的obj，
要求设计它们的interface以实现取款机的登录，取钱，存钱等func
