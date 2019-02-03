<?php
    require __DIR__ . '/lib/MinecraftPing.php';
    require __DIR__ . '/lib/MinecraftPingException.php';
    header('Content-Type: application/json');
    try
    {
        $Query = new MinecraftPing( 'dimicraft.tk', 25560 );

        echo json_encode($Query->Query());
    }
    catch( MinecraftPingException $e )
    {
        echo json_encode($e->getMessage());
    }
    finally
    {
        $Query->Close();
    }
?>
