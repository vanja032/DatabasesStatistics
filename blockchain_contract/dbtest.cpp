#include "dbtest.hpp"

[[inery::action]] void dbtest::insert( string f_name, string l_name, string email, string gender ){
    require_auth(get_self());
    usersts.emplace( _self, [&]( auto& u ) {
        u.user_id = usersts.available_primary_key();
        u.f_name = f_name;
        u.l_name = l_name;
        u.email = email;
        u.gender = gender;
    });
}

[[inery::action]] void dbtest::update( uint64_t user_id, string f_name, string l_name, string email, string gender ){
    require_auth(get_self());
    auto uit = usersts.find(user_id);
    if(uit != usersts.end()){
        usersts.modify( uit, _self, [&]( auto& u ) {
            u.f_name = f_name;
            u.l_name = l_name;
            u.email = email;
            u.gender = gender;
        });
    }
    
}

[[inery::action]] void dbtest::remove( uint64_t user_id ){
    require_auth(get_self());
    auto uit = usersts.find(user_id);
    if(uit != usersts.end()){
        usersts.erase( uit );
    }
}