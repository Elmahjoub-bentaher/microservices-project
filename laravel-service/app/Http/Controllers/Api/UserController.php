<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Http\Request;

class UserController extends Controller
{
    // Lister tous les utilisateurs
    public function index()
    {
        $users = User::all();
        return response()->json($users);
    }

    // Créer un nouvel utilisateur
    public function store(Request $request)
    {
        $data = $request->all();
        $data['password'] = bcrypt($request->password);  // Hacher le mot de passe
        $user = User::create($data);
        return response()->json($user, 201);
    }

    // Récupérer un utilisateur par son ID
    public function show($id)
    {
        $user = User::findOrFail($id);
        return response()->json($user);
    }

    // Mettre à jour un utilisateur
    public function update(Request $request, $id)
    {
        $user = User::findOrFail($id);
        $data = $request->all();
        if ($request->has('password')) {
            $data['password'] = bcrypt($request->password);  // Hacher le mot de passe
        }
        $user->update($data);
        return response()->json($user);
    }

    // Supprimer un utilisateur
    public function destroy($id)
    {
        User::destroy($id);
        return response()->json(null, 204);
    }
}