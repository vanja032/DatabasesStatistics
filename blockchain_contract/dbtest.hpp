#include <inery/inery.hpp>
using namespace inery;
using namespace std;

class [[inery::contract]] dbtest : public contract {
    public:
        using contract::contract;

        struct [[inery::table]] users {
            uint64_t user_id;
            string f_name;
            string l_name;
            string email;
            string gender;
            uint64_t primary_key( ) const { return user_id; }
        };

        typedef inery::multi_index<"users"_n, users> users_t;

        users_t usersts;

        dbtest( name receiver, name code, datastream<const char*> ds ) : 
        contract(receiver, code, ds), 
        usersts(receiver, receiver.value)
        { }

        [[inery::action]] void insert( string f_name, string l_name, string email, string gender );
        [[inery::action]] void update( uint64_t user_id, string f_name, string l_name, string email, string gender );
        [[inery::action]] void remove( uint64_t user_id );

        using insert_action = action_wrapper<"insert"_n, &dbtest::insert>;
        using update_action = action_wrapper<"update"_n, &dbtest::update>;
        using remove_action = action_wrapper<"remove"_n, &dbtest::remove>;
};